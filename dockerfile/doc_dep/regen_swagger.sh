#!/bin/sh

set -e

if [ -z "$SWAGGER_CODEGEN_CLI_JAR" ]; then
	echo "SWAGGER_CODEGEN_CLI_JAR not set"
	exit 1
fi

rm -rf generated

mkdir -p generated/client generated/docs

product_name=${PRODUCT_NAME:-all}
config_file=config/swagger_${product_name}_config.yaml

ruby merge_swagger.rb "$@" -f "${config_file}" || exit 1
ruby merge_swagger.rb "$@" -l en -f "${config_file}" || exit 1

npx @redocly/cli build-docs generated/wati-aigc-openapi.swagger.json -o generated/docs/index.html

if [[ -n ${SKIP_CLIENT_GEN} ]]; then
    echo "Skipping client generators..."
    exit 0
fi

ruby merge_swagger_for_client.rb "$@" -f "${config_file}" || exit 1
ruby merge_swagger_for_client.rb "$@" -l en -f "${config_file}" || exit 1

out=generated/wati-aigc-openapi-for-client.swagger.json

for lang in "python" "java"; do
    java -jar $SWAGGER_CODEGEN_CLI_JAR generate -i $out -l $lang\
        -o generated/client/$lang -c generated/swagger-config-$lang.json
done

# python client has bugs
sed -i "/collection_formats\['file'\]/d" generated/client/python/doclib_openapi/api/data_ingress_service_api.py
sed -i "s/^.*form_params.append(('file'.*$/            local_var_files['file'] = params['file']/" generated/client/python/doclib_openapi/api/data_ingress_service_api.py