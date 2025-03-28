# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api-proxy-service/api.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'api-proxy-service/api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2
import commi_pb2 as commi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pi-proxy-service/api.proto\x12+wati.ai_platform.protocol.api_proxy_service\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\x1a\x0b\x63ommi.proto\"\x97\x02\n\x18VideoTemplateListRequest\x12?\n\x06paging\x18\x01 \x01(\x0b\x32/.wati.ai_platform.protocol.common.RequestPaging\x12;\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32).wati.ai_platform.protocol.commi.CATEGORY\x12\x39\n\x04name\x18\x03 \x01(\x0b\x32+.wati.ai_platform.protocol.common.NameQuery\x12\x42\n\tfavourite\x18\x04 \x01(\x0e\x32/.wati.ai_platform.protocol.common.USERFAVOURITE\"g\n\x06Script\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12L\n\nparameters\x18\x02 \x03(\x0b\x32\x38.wati.ai_platform.protocol.commi.TemplateScriptParameter\"\xf7\x02\n\x08Template\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12;\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32).wati.ai_platform.protocol.commi.CATEGORY\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x42\n\tfavourite\x18\x07 \x01(\x0e\x32/.wati.ai_platform.protocol.common.USERFAVOURITE\x12\x43\n\x06script\x18\x08 \x01(\x0b\x32\x33.wati.ai_platform.protocol.api_proxy_service.Script\x12-\n\tcreate_at\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdate_at\x18  \x01(\x0b\x32\x1a.google.protobuf.TimestampJ\x04\x08\t\x10\nJ\x04\x08\x1e\x10\x1f\"\xa7\x01\n\x19VideoTemplateListResponse\x12H\n\ttemplates\x18\x01 \x03(\x0b\x32\x35.wati.ai_platform.protocol.api_proxy_service.Template\x12@\n\x06paging\x18\x02 \x01(\x0b\x32\x30.wati.ai_platform.protocol.common.ResponsePaging\".\n\x17VideoTemplateGetRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\"c\n\x18VideoTemplateGetResponse\x12G\n\x08template\x18\x01 \x01(\x0b\x32\x35.wati.ai_platform.protocol.api_proxy_service.Template\"v\n\x1eVideoTemplateScriptListRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12?\n\x06paging\x18\x02 \x01(\x0b\x32/.wati.ai_platform.protocol.common.RequestPaging\"\xa5\x01\n\x1fVideoTemplateScriptListResponse\x12@\n\x07scripts\x18\x01 \x03(\x0b\x32/.wati.ai_platform.protocol.commi.TemplateScript\x12@\n\x06paging\x18\x02 \x01(\x0b\x32\x30.wati.ai_platform.protocol.common.ResponsePaging\"G\n\x1dVideoTemplateScriptGetRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12\x11\n\tscript_id\x18\x02 \x01(\t\"a\n\x1eVideoTemplateScriptGetResponse\x12?\n\x06script\x18\x01 \x01(\x0b\x32/.wati.ai_platform.protocol.commi.TemplateScript\"\x91\x02\n\x12SpeakerListRequest\x12?\n\x06paging\x18\x01 \x01(\x0b\x32/.wati.ai_platform.protocol.common.RequestPaging\x12\x39\n\x04name\x18\x02 \x01(\x0b\x32+.wati.ai_platform.protocol.common.NameQuery\x12;\n\x08language\x18\x03 \x01(\x0e\x32).wati.ai_platform.protocol.commi.LANGUAGE\x12\x42\n\tfavourite\x18\x04 \x01(\x0e\x32/.wati.ai_platform.protocol.common.USERFAVOURITE\"\x99\x03\n\x07Speaker\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\x08language\x18\x03 \x01(\x0e\x32).wati.ai_platform.protocol.commi.LANGUAGE\x12\x38\n\x06gender\x18\x04 \x01(\x0e\x32(.wati.ai_platform.protocol.common.GENDER\x12\x19\n\x11\x61udio_sample_name\x18\x05 \x01(\t\x12\x34\n\x04tone\x18\x06 \x01(\x0e\x32&.wati.ai_platform.protocol.common.TONE\x12\x42\n\tfavourite\x18\x07 \x01(\x0e\x32/.wati.ai_platform.protocol.common.USERFAVOURITE\x12-\n\tcreate_at\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdate_at\x18  \x01(\x0b\x32\x1a.google.protobuf.TimestampJ\x04\x08\x08\x10\tJ\x04\x08\x1e\x10\x1f\"\x9f\x01\n\x13SpeakerListResponse\x12\x46\n\x08speakers\x18\x01 \x03(\x0b\x32\x34.wati.ai_platform.protocol.api_proxy_service.Speaker\x12@\n\x06paging\x18\x02 \x01(\x0b\x32\x30.wati.ai_platform.protocol.common.ResponsePaging\"\x1f\n\x11SpeakerGetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"[\n\x12SpeakerGetResponse\x12\x45\n\x07speaker\x18\x01 \x01(\x0b\x32\x34.wati.ai_platform.protocol.api_proxy_service.Speaker\"\xd1\x04\n\x05Video\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tvideo_url\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\x05\x12;\n\x08\x63\x61tegory\x18\x06 \x01(\x0e\x32).wati.ai_platform.protocol.commi.CATEGORY\x12\x13\n\x0btemplate_id\x18\x07 \x01(\t\x12\x12\n\nspeaker_id\x18\x08 \x01(\t\x12\x61\n\x10script_parameter\x18\x0b \x03(\x0b\x32G.wati.ai_platform.protocol.api_proxy_service.Video.ScriptParameterEntry\x12\x34\n\x04tone\x18\x0c \x01(\x0e\x32&.wati.ai_platform.protocol.common.TONE\x12<\n\x06status\x18\r \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12-\n\tcreate_at\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdate_at\x18  \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x36\n\x14ScriptParameterEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0e\x10\x0fJ\x04\x08\x1e\x10\x1fR\tscript_id\"\xab\x02\n\x10VideoListRequest\x12<\n\x06status\x18\x01 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12\x14\n\x0cis_ascending\x18\x02 \x01(\x08\x12;\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32).wati.ai_platform.protocol.commi.CATEGORY\x12\x39\n\x04name\x18\x04 \x01(\x0b\x32+.wati.ai_platform.protocol.common.NameQuery\x12?\n\x06paging\x18\x15 \x01(\x0b\x32/.wati.ai_platform.protocol.common.RequestPagingJ\x04\x08\x05\x10\x06J\x04\x08\x14\x10\x15\"\x99\x01\n\x11VideoListResponse\x12\x42\n\x06videos\x18\x01 \x03(\x0b\x32\x32.wati.ai_platform.protocol.api_proxy_service.Video\x12@\n\x06paging\x18\x02 \x01(\x0b\x32\x30.wati.ai_platform.protocol.common.ResponsePaging\"\xee\x02\n\x13VideoNewTaskRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0btemplate_id\x18\x03 \x01(\t\x12o\n\x10script_parameter\x18\x05 \x03(\x0b\x32U.wati.ai_platform.protocol.api_proxy_service.VideoNewTaskRequest.ScriptParameterEntry\x12\x12\n\nspeaker_id\x18\x06 \x01(\t\x12\x34\n\x04tone\x18\x07 \x01(\x0e\x32&.wati.ai_platform.protocol.common.TONE\x12\x1b\n\x13result_callback_url\x18\x08 \x01(\t\x1a\x36\n\x14ScriptParameterEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x04\x10\x05R\tscript_id\"`\n\x14VideoNewTaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12<\n\x06status\x18\x02 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\"-\n\x19VideoTaskStatusGetRequest\x12\x10\n\x08video_id\x18\x01 \x01(\t\"\x83\x01\n\x1aVideoTaskStatusGetResponse\x12<\n\x06status\x18\x01 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0e\x65stimated_time\x18\x03 \x01(\x03\"#\n\x0fVideoGetRequest\x12\x10\n\x08video_id\x18\x01 \x01(\t\"U\n\x10VideoGetResponse\x12\x41\n\x05video\x18\x01 \x01(\x0b\x32\x32.wati.ai_platform.protocol.api_proxy_service.Video\"I\n\x12VideoUpdateRequest\x12\x10\n\x08video_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"X\n\x13VideoUpdateResponse\x12\x41\n\x05video\x18\x01 \x01(\x0b\x32\x32.wati.ai_platform.protocol.api_proxy_service.Video\"&\n\x12VideoDeleteRequest\x12\x10\n\x08video_id\x18\x01 \x01(\t\"\x15\n\x13VideoDeleteResponse\".\n\x0fWatiCustomParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xc9\x01\n\x16SendWATIMessageRequest\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x16\n\x0e\x62roadcast_name\x18\x03 \x01(\t\x12\x15\n\rtemplate_name\x18\x04 \x01(\t\x12\x15\n\rvariable_name\x18\x05 \x01(\t\x12\x41\n\treceivers\x18\x06 \x03(\x0b\x32..wati.ai_platform.protocol.common.WatiReceiver\"Q\n\x17SendWATIMessageResponse\x12\x36\n\x04rets\x18\x01 \x03(\x0b\x32(.wati.ai_platform.protocol.common.Result2\xd9\x0f\n\x0f\x41PIProxyService\x12\xbf\x01\n\x11VideoTemplateList\x12\x45.wati.ai_platform.protocol.api_proxy_service.VideoTemplateListRequest\x1a\x46.wati.ai_platform.protocol.api_proxy_service.VideoTemplateListResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/video/templates\x12\xca\x01\n\x10VideoTemplateGet\x12\x44.wati.ai_platform.protocol.api_proxy_service.VideoTemplateGetRequest\x1a\x45.wati.ai_platform.protocol.api_proxy_service.VideoTemplateGetResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/video/templates/{template_id}\x12\xa6\x01\n\x0bSpeakerList\x12?.wati.ai_platform.protocol.api_proxy_service.SpeakerListRequest\x1a@.wati.ai_platform.protocol.api_proxy_service.SpeakerListResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/speakers\x12\xa8\x01\n\nSpeakerGet\x12>.wati.ai_platform.protocol.api_proxy_service.SpeakerGetRequest\x1a?.wati.ai_platform.protocol.api_proxy_service.SpeakerGetResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/speakers/{id}\x12\x9e\x01\n\tVideoList\x12=.wati.ai_platform.protocol.api_proxy_service.VideoListRequest\x1a>.wati.ai_platform.protocol.api_proxy_service.VideoListResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/videos\x12\xa6\x01\n\x08VideoGet\x12<.wati.ai_platform.protocol.api_proxy_service.VideoGetRequest\x1a=.wati.ai_platform.protocol.api_proxy_service.VideoGetResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/videos/{video_id}\x12\xaa\x01\n\x0cVideoTaskNew\x12@.wati.ai_platform.protocol.api_proxy_service.VideoNewTaskRequest\x1a\x41.wati.ai_platform.protocol.api_proxy_service.VideoNewTaskResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v1/videos:\x01*\x12\xcb\x01\n\x12VideoTaskStatusGet\x12\x46.wati.ai_platform.protocol.api_proxy_service.VideoTaskStatusGetRequest\x1aG.wati.ai_platform.protocol.api_proxy_service.VideoTaskStatusGetResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/videos/{video_id}/status\x12\xb2\x01\n\x0bVideoUpdate\x12?.wati.ai_platform.protocol.api_proxy_service.VideoUpdateRequest\x1a@.wati.ai_platform.protocol.api_proxy_service.VideoUpdateResponse\" \x82\xd3\xe4\x93\x02\x1a\x32\x15/v1/videos/{video_id}:\x01*\x12\xaf\x01\n\x0bVideoDelete\x12?.wati.ai_platform.protocol.api_proxy_service.VideoDeleteRequest\x1a@.wati.ai_platform.protocol.api_proxy_service.VideoDeleteResponse\"\x1d\x82\xd3\xe4\x93\x02\x17*\x15/v1/videos/{video_id}\x12\xb6\x01\n\x0fSendWATIMessage\x12\x43.wati.ai_platform.protocol.api_proxy_service.SendWATIMessageRequest\x1a\x44.wati.ai_platform.protocol.api_proxy_service.SendWATIMessageResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/send/wati:\x01*B^Z=github.com/ClareAI/ai-platform-protocol/api/api-proxy-service\x92\x41\x1c\x12\x1a\n\x11\x41PI Proxy Service2\x05\x31.0.0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_proxy_service.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/ClareAI/ai-platform-protocol/api/api-proxy-service\222A\034\022\032\n\021API Proxy Service2\0051.0.0'
  _globals['_VIDEO_SCRIPTPARAMETERENTRY']._loaded_options = None
  _globals['_VIDEO_SCRIPTPARAMETERENTRY']._serialized_options = b'8\001'
  _globals['_VIDEONEWTASKREQUEST_SCRIPTPARAMETERENTRY']._loaded_options = None
  _globals['_VIDEONEWTASKREQUEST_SCRIPTPARAMETERENTRY']._serialized_options = b'8\001'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTemplateList']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTemplateList']._serialized_options = b'\202\323\344\223\002\025\022\023/v1/video/templates'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTemplateGet']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTemplateGet']._serialized_options = b'\202\323\344\223\002#\022!/v1/video/templates/{template_id}'
  _globals['_APIPROXYSERVICE'].methods_by_name['SpeakerList']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['SpeakerList']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/speakers'
  _globals['_APIPROXYSERVICE'].methods_by_name['SpeakerGet']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['SpeakerGet']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/speakers/{id}'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoList']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoList']._serialized_options = b'\202\323\344\223\002\014\022\n/v1/videos'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoGet']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoGet']._serialized_options = b'\202\323\344\223\002\027\022\025/v1/videos/{video_id}'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTaskNew']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTaskNew']._serialized_options = b'\202\323\344\223\002\017\"\n/v1/videos:\001*'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTaskStatusGet']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoTaskStatusGet']._serialized_options = b'\202\323\344\223\002\036\022\034/v1/videos/{video_id}/status'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoUpdate']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoUpdate']._serialized_options = b'\202\323\344\223\002\0322\025/v1/videos/{video_id}:\001*'
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoDelete']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['VideoDelete']._serialized_options = b'\202\323\344\223\002\027*\025/v1/videos/{video_id}'
  _globals['_APIPROXYSERVICE'].methods_by_name['SendWATIMessage']._loaded_options = None
  _globals['_APIPROXYSERVICE'].methods_by_name['SendWATIMessage']._serialized_options = b'\202\323\344\223\002\022\"\r/v1/send/wati:\001*'
  _globals['_VIDEOTEMPLATELISTREQUEST']._serialized_start=215
  _globals['_VIDEOTEMPLATELISTREQUEST']._serialized_end=494
  _globals['_SCRIPT']._serialized_start=496
  _globals['_SCRIPT']._serialized_end=599
  _globals['_TEMPLATE']._serialized_start=602
  _globals['_TEMPLATE']._serialized_end=977
  _globals['_VIDEOTEMPLATELISTRESPONSE']._serialized_start=980
  _globals['_VIDEOTEMPLATELISTRESPONSE']._serialized_end=1147
  _globals['_VIDEOTEMPLATEGETREQUEST']._serialized_start=1149
  _globals['_VIDEOTEMPLATEGETREQUEST']._serialized_end=1195
  _globals['_VIDEOTEMPLATEGETRESPONSE']._serialized_start=1197
  _globals['_VIDEOTEMPLATEGETRESPONSE']._serialized_end=1296
  _globals['_VIDEOTEMPLATESCRIPTLISTREQUEST']._serialized_start=1298
  _globals['_VIDEOTEMPLATESCRIPTLISTREQUEST']._serialized_end=1416
  _globals['_VIDEOTEMPLATESCRIPTLISTRESPONSE']._serialized_start=1419
  _globals['_VIDEOTEMPLATESCRIPTLISTRESPONSE']._serialized_end=1584
  _globals['_VIDEOTEMPLATESCRIPTGETREQUEST']._serialized_start=1586
  _globals['_VIDEOTEMPLATESCRIPTGETREQUEST']._serialized_end=1657
  _globals['_VIDEOTEMPLATESCRIPTGETRESPONSE']._serialized_start=1659
  _globals['_VIDEOTEMPLATESCRIPTGETRESPONSE']._serialized_end=1756
  _globals['_SPEAKERLISTREQUEST']._serialized_start=1759
  _globals['_SPEAKERLISTREQUEST']._serialized_end=2032
  _globals['_SPEAKER']._serialized_start=2035
  _globals['_SPEAKER']._serialized_end=2444
  _globals['_SPEAKERLISTRESPONSE']._serialized_start=2447
  _globals['_SPEAKERLISTRESPONSE']._serialized_end=2606
  _globals['_SPEAKERGETREQUEST']._serialized_start=2608
  _globals['_SPEAKERGETREQUEST']._serialized_end=2639
  _globals['_SPEAKERGETRESPONSE']._serialized_start=2641
  _globals['_SPEAKERGETRESPONSE']._serialized_end=2732
  _globals['_VIDEO']._serialized_start=2735
  _globals['_VIDEO']._serialized_end=3328
  _globals['_VIDEO_SCRIPTPARAMETERENTRY']._serialized_start=3239
  _globals['_VIDEO_SCRIPTPARAMETERENTRY']._serialized_end=3293
  _globals['_VIDEOLISTREQUEST']._serialized_start=3331
  _globals['_VIDEOLISTREQUEST']._serialized_end=3630
  _globals['_VIDEOLISTRESPONSE']._serialized_start=3633
  _globals['_VIDEOLISTRESPONSE']._serialized_end=3786
  _globals['_VIDEONEWTASKREQUEST']._serialized_start=3789
  _globals['_VIDEONEWTASKREQUEST']._serialized_end=4155
  _globals['_VIDEONEWTASKREQUEST_SCRIPTPARAMETERENTRY']._serialized_start=3239
  _globals['_VIDEONEWTASKREQUEST_SCRIPTPARAMETERENTRY']._serialized_end=3293
  _globals['_VIDEONEWTASKRESPONSE']._serialized_start=4157
  _globals['_VIDEONEWTASKRESPONSE']._serialized_end=4253
  _globals['_VIDEOTASKSTATUSGETREQUEST']._serialized_start=4255
  _globals['_VIDEOTASKSTATUSGETREQUEST']._serialized_end=4300
  _globals['_VIDEOTASKSTATUSGETRESPONSE']._serialized_start=4303
  _globals['_VIDEOTASKSTATUSGETRESPONSE']._serialized_end=4434
  _globals['_VIDEOGETREQUEST']._serialized_start=4436
  _globals['_VIDEOGETREQUEST']._serialized_end=4471
  _globals['_VIDEOGETRESPONSE']._serialized_start=4473
  _globals['_VIDEOGETRESPONSE']._serialized_end=4558
  _globals['_VIDEOUPDATEREQUEST']._serialized_start=4560
  _globals['_VIDEOUPDATEREQUEST']._serialized_end=4633
  _globals['_VIDEOUPDATERESPONSE']._serialized_start=4635
  _globals['_VIDEOUPDATERESPONSE']._serialized_end=4723
  _globals['_VIDEODELETEREQUEST']._serialized_start=4725
  _globals['_VIDEODELETEREQUEST']._serialized_end=4763
  _globals['_VIDEODELETERESPONSE']._serialized_start=4765
  _globals['_VIDEODELETERESPONSE']._serialized_end=4786
  _globals['_WATICUSTOMPARAM']._serialized_start=4788
  _globals['_WATICUSTOMPARAM']._serialized_end=4834
  _globals['_SENDWATIMESSAGEREQUEST']._serialized_start=4837
  _globals['_SENDWATIMESSAGEREQUEST']._serialized_end=5038
  _globals['_SENDWATIMESSAGERESPONSE']._serialized_start=5040
  _globals['_SENDWATIMESSAGERESPONSE']._serialized_end=5121
  _globals['_APIPROXYSERVICE']._serialized_start=5124
  _globals['_APIPROXYSERVICE']._serialized_end=7133
# @@protoc_insertion_point(module_scope)
