require 'json'
require 'yaml'
require 'optparse'

def parse_version(s)
  if s.nil? || s == ''
    return nil
  end
  if /^v(\d+)\.(\d+)\.(\d+)$/ =~ s
    x = $1.to_i
    y = $2.to_i
    z = $3.to_i
    v = x * 1000 * 1000 + y * 1000 + z
    # STDERR.puts v
    return v
  else
    STDERR.puts "invalid version string: '#{s}'"
    return nil
  end
end

def parse_internal(s)
  return nil if s.nil? || s == ''
  re = /\[INTERNAL\]/i
  return re =~ s
end

def parse_version_in_desc(s)
  if s.nil? || s == ''
    return nil
  end
  re = /\[SINCE\s+(.+?)\]/i
  if re =~ s
    return parse_version($1)
  end
  return nil
end

def parse_doc(s, lang)
  return s if s.nil? || s == ""
  arr = s.split('[EN]')
  if arr.length >= 2
    if lang == "cn"
      arr[0].strip
    else
      arr[1].strip
    end
  else
    STDERR.puts "WARNING: no translation: #{s}" if lang == "en"
    s.strip
  end
end

def parse_one_enum_item(e, lang, is_title)
  hidden = false
  if !is_title
    showAll = GOPTIONS[:show_all]
    if !showAll && GOPTIONS[:version_str] && parse_internal(e)
      hidden = true
    end

    since = parse_version_in_desc(e) || 0
    if !showAll && since > GSYS_VERSION
      STDERR.puts "Skipping enum item: #{e}"
      hidden = true
    end
  end

  if e =~ /^([A-Z_][a-zA-Z0-9_]+):/
    name=$1
    [name, "#{name}: #{parse_doc(e[name.length+1..-1], lang)}", hidden]
  else
    ["", parse_doc(e, lang), hidden]
  end
end

def parse_enum_doc(s, lang)
  return s if s.nil? || s == ""
  is_title = true
  # no description
  if s.start_with?(' - ')
      s = "\n" + s
      is_title = false
  end
  hiddens = {}
  docs = s.split("\n - ").map{|e|
    name, doc, hidden = parse_one_enum_item(e, lang, is_title)
    if hidden && !name.empty?
      hiddens[name] = true
    end
    is_title = false
    hidden ? nil : doc
  }.reject(&:nil?).join("\n - ")
  [docs, hiddens]
end

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: merge_swagger.rb [options]"
  opts.on("-v", "--version [VERSION]", "set viper version") do |v|
    options[:version] = parse_version(v)
    options[:version_str] = v
  end

  opts.on("-h", "--help", "Show this message") do
    puts opts
    exit 1
  end

  opts.on("-l", "--language [LANG]", "Language") do |v|
    options[:lang] = v
  end

  opts.on("-f", "--input-file [FILENAME]", "Input file name") do |v|
    options[:input] = v
  end

  opts.on("-s", "--show-all", "show all even if version is set") do |v|
    options[:show_all] = v
  end
end.parse!

conf = YAML.load(File.read(options[:input]))
sysVersion = options[:version] || 9999999999
showAll = options[:show_all]
lang = options[:lang] || "cn"

basePath = conf['basePath'] || File.dirname(ARGV[0])

logo = {
  'url' => "./logo.png",
  'backgroundColor' => "#FFFFFF",
}

doc = {}
doc['swagger'] = "2.0"
doc['info'] = {
  'title' => conf["title"] || "No title",
  'x-logo' =>  logo,
  'version' => options[:version_str] || conf["version"] || "No version",
}
doc['schemes'] = ['http', 'https']
doc['consumes'] = ['application/json']
doc['produces'] = ['application/json']

['contact', 'license'].each do |e|
  doc['info'][e] = conf[e]
end

GOPTIONS = options
GSYS_VERSION = sysVersion

paths = {}
defs = {}

def underscore(camel_cased_word)
  camel_cased_word.to_s.gsub(/::/, '/').
    gsub(/([A-Z]+)([A-Z][a-z])/,'\1_\2').
    gsub(/([a-z\d])([A-Z])/,'\1_\2').
    tr("-", "_").
    downcase
end

def replace_all_ref(h, m)
  h.each do |k, v|
    if k == '$ref' && v.is_a?(String)
      t = v.split('/').last
      newv = v
      newv.gsub!("/#{t}", "/#{m[t]}") if m[t]
      h['$ref'] = newv
    elsif v.is_a?(Hash)
      replace_all_ref(v, m)
    elsif v.is_a?(Array)
      v.each do |e|
        replace_all_ref(e, m) if e.is_a?(Hash)
      end
    end
  end
end

def render_tag(t, v)
  return """
## #{t}
#{v['title'] || "No title"}

#{v['description'] || "No description"}

Version: #{v['version'] || "No version"} | Since: #{v['since'] || "v1.0.0"} | [Doc](#tag-#{t})
"""
end

tags = {}

conf['modules'].each do |k, v|
  # guess base
  base = k

  sinceVer = parse_version(v['since']) || 0
  if !showAll && sinceVer > sysVersion
    STDERR.puts "Skipping #{k}: #{v['since']}"
    next
  end
  if !showAll && options[:version_str] && v['internal']
    STDERR.puts "Skipping internal: #{k}"
    next
  end

  STDERR.puts "Processing: #{v['ref']}"
  fpath = File.join(basePath, v['ref'])
  d = JSON.load(File.read(fpath))

  newpaths = {}
  ftags = []

  urlBase = v['urlBase'] || ""
  urlParams = v['urlParams'] || {}
  defaultUrlParams = {
    'in' => 'path',
    'require' => true,
    'type' => 'string',
  }
  urlParams.each do |k, v|
    v.merge!(defaultUrlParams)
    v['name'] = k
    v['description'] = parse_doc(v['description'], lang) if v['description']
  end

  extra = {}
  if v['extra']
    fpath = File.join(basePath, v['extra'])
    extra = JSON.load(File.read(fpath))
    # d['paths'].merge!(extra['paths'])
    d['definitions'].merge!(extra['definitions'])
  end

  override = v['overrideUrlBase'] || {}
  d['paths'].each do |k, v|
    if extra['paths'] && extra['paths'][k]
      d['paths'][k].merge!(extra['paths'][k])
    end

    apitag = nil
    unless apitag
      v.each do |verb, v|
        apitag = v['tags'].first
      end
    end

    urlBaseNew = urlBase
    if override[apitag]
      urlBaseNew = override[apitag]
    end

    p = urlBaseNew + k
    skipped = false

    v.each do |verb, v|
      oid = v['operationId']
      since = parse_version_in_desc(v['summary']) || 0
      if !showAll && since > sysVersion
        STDERR.puts "Skipping operation: #{k} #{oid}"
        skipped = true
        break
      end
      if !showAll && options[:version_str] && parse_internal(v['summary'])
        STDERR.puts "Skipping internal operation: #{k} #{oid}"
        skipped = true
        break
      end
      v['operationId'] = base + oid if oid
      v['description'] = parse_doc(v['summary'], lang)
      v['summary'] = oid
      v['responses'] ||= []
      v['responses'].each do |code, resp|
        resp['description'] = parse_doc(resp['description'], lang) if resp['description']
        if resp['description'] && resp['description'] != "" && resp['schema']
          resp['schema'] = {"allOf" => [{"$ref" => resp['schema']["$ref"]}]}
        end
      end
      v['parameters'] ||= []
      v['parameters'].each do |e|
        e['description'] = parse_doc(e['description'], lang) if e['description']
        if e['description'] && e['description'] != "" && e['schema']
          e['schema'] = {"allOf" => [{"$ref" => e['schema']["$ref"]}]}
        end
      end
      urlParams.each do |k, p|
        v['parameters'] << p
      end
      STDERR.puts "Not tags: #{k} #{verb}" unless v['tags']
    end
    next if skipped

    newpaths[p] = v
    v.each do |verb, v|
      tag = v['tags'].first
      ftags << tag if tag && !ftags.include?(tag)
    end
  end
  if !ftags.empty?
    d['info']['since'] = v['since']
    ftags.each {|e| tags[e] = d['info']}
  end

  # d['paths'].each do |k|
  #   STDERR.puts "#{k} already have" if paths[k]
  # end

  paths.merge!(newpaths)
  rep = {}
  onedef = d['definitions']

  newdef = {}
  onedef.each do |k,v|
    if v['enum']
      if v['description']
        v['description'], hiddens = parse_enum_doc(v['description'], lang)
        if hiddens.size > 0
          STDERR.puts "hide enum item: ", hiddens
        end
        v['enum'].delete_if{|e| hiddens[e] && e != v['default']}
      end
    else
      v['description'] = parse_doc(v['description'], lang) if v['description']
    end
    if v['properties']
      v['properties'].delete_if { |f, e|
        since = parse_version_in_desc(e['description']) || 0
        if !showAll && since > sysVersion
          STDERR.puts "Skipping field: #{f}"
          true
        else
          false
        end
      }
      v['properties'].each { |k, v|
        v['description'] = parse_doc(v['description'], lang) if v['description']
        if v['description'] && v['description'] != "" && v['$ref']
          v['allOf'] = [{"$ref" => v["$ref"]}]
          v.delete('$ref')
        end
      }
    end
    # TODO skip enum field
    if k[0] =~ /[A-Z]/
      newk = underscore(base) + '_inner' + k
      rep[k] = newk
      newdef[newk] = v
    else
      newdef[k] = v
      # puts k
    end
  end

  replace_all_ref(d, rep)
  defs.merge!(newdef)
end

doc['paths'] = paths
doc['definitions'] = defs

desc = File.read(conf["description"]) || "No description"
desc += "\r\n"
tags.keys.sort.each do |k|
  desc += render_tag(k, tags[k])
end
doc['info']['description'] = desc

doc['tags'] = []
tags.each do |k,v|
  doc['tags'] << {
    'name' => k,
  }
end
doc['tags'].sort_by! {|e| e['name'] }
# doc['tags'].each {|e| p e['name']}

swaggerfn = "generated/wati-aigc-openapi.swagger.json"
if lang == "en"
  swaggerfn = "generated/wati-aigc-openapi-en.swagger.json"
end
File.open(swaggerfn, "wb") do |w|
  w.write JSON.pretty_generate(doc)
end

# Write lang configs

File.open("generated/swagger-config-python.json", "wb") do |w|
  cfg = {
    'packageName' => conf['codegen']['pythonPackageName'],
    'projectName' => conf['codegen']['pythonPackageName'].gsub('_','-')
  }
  w.write JSON.pretty_generate(cfg)
end

File.open("generated/swagger-config-java.json", "wb") do |w|
  cfg = {
    'apiPackage' => conf['codegen']['javaGroupId']+".api",
    'modelPackage' => conf['codegen']['javaGroupId']+".model",
  }
  w.write JSON.pretty_generate(cfg)
end

File.open("generated/swagger-config-html2.json", "wb") do |w|
  cfg = {
    'pythonPackageName' => conf['codegen']['pythonPackageName'],
    'invokerPackage' => conf['codegen']['javaGroupId'],
    'groupId' => conf['codegen']['javaGroupId'],
    'artifactId' => conf['codegen']['javaArtifactId'],
  }
  w.write JSON.pretty_generate(cfg)
end



