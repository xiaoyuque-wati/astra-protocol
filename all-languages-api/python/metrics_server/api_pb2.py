# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: metrics-server/api.proto
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
    'metrics-server/api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2
import commi_pb2 as commi__pb2
import movideo_pb2 as movideo__pb2
import task_pb2 as task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18metrics-server/api.proto\x12(wati.ai_platform.protocol.metrics_server\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\x1a\x0b\x63ommi.proto\x1a\rmovideo.proto\x1a\ntask.proto\"T\n\x10\x43ommiUserNewInfo\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x31\n\rregister_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xff\x01\n\x13\x43ommiUserActiveInfo\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05phone\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\x13\n\x0binformation\x18\x06 \x01(\t\x12\x16\n\x0einitial_credit\x18\x07 \x01(\x02\x12<\n\x06source\x18\x08 \x01(\x0e\x32,.wati.ai_platform.protocol.common.USERSOURCE\x12\x34\n\x10\x66irst_login_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa9\x06\n\x18\x43ommiVideoGenerationInfo\x12\x10\n\x08video_id\x18\x01 \x01(\t\x12\x12\n\nvideo_name\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08interval\x18\x06 \x01(\x05\x12<\n\x06result\x18\x07 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12\x13\n\x0btemplate_id\x18\x08 \x01(\t\x12\x15\n\rtemplate_name\x18\t \x01(\t\x12;\n\x08\x63\x61tegory\x18\n \x01(\x0e\x32).wati.ai_platform.protocol.commi.CATEGORY\x12\x12\n\nspeaker_id\x18\x0b \x01(\t\x12\x14\n\x0cspeaker_name\x18\x0c \x01(\t\x12;\n\x08language\x18\r \x01(\x0e\x32).wati.ai_platform.protocol.commi.LANGUAGE\x12\x19\n\x11script_word_count\x18\x0e \x01(\x05\x12\x17\n\x0ftemplate_script\x18\x0f \x01(\t\x12\x0e\n\x06script\x18\x10 \x01(\t\x12q\n\x10script_variables\x18\x11 \x03(\x0b\x32W.wati.ai_platform.protocol.metrics_server.CommiVideoGenerationInfo.ScriptVariablesEntry\x12\x16\n\x0evideo_duration\x18\x12 \x01(\x05\x12<\n\x06source\x18\x13 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSOURCE\x12\x13\n\x0b\x63redit_cost\x18\x14 \x01(\x02\x1a\x36\n\x14ScriptVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbc\x01\n\x15\x43ommiAPIKeyActionInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\napi_key_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61pi_key_name\x18\x03 \x01(\t\x12>\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32..wati.ai_platform.protocol.common.APIKEYACTION\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbc\x01\n\x11\x43ommiAPIUsageInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\napi_key_id\x18\x02 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\x13\n\x0bstatus_code\x18\x05 \x01(\x05\x12\x16\n\x0estatus_message\x18\x06 \x01(\t\x12\x33\n\x0finvocation_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x83\x02\n\x13\x43ommiVideoShareInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08video_id\x18\x02 \x01(\t\x12\x11\n\tvideo_url\x18\x03 \x01(\t\x12\x1a\n\x12wati_template_name\x18\x04 \x01(\t\x12\x1b\n\x13wati_broadcast_name\x18\x05 \x01(\t\x12\x17\n\x0fwhatsapp_number\x18\x06 \x01(\t\x12\x18\n\x10send_status_code\x18\x07 \x01(\x05\x12\x1b\n\x13send_status_message\x18\x08 \x01(\t\x12-\n\tsend_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8f\x02\n\x14\x43ommiCreditEventInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x41\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x31.wati.ai_platform.protocol.common.USERCREDITEVENT\x12;\n\titem_type\x18\x03 \x01(\x0e\x32(.wati.ai_platform.protocol.task.ITEMTYPE\x12\x0f\n\x07item_id\x18\x04 \x01(\t\x12\x15\n\rchange_amount\x18\x05 \x01(\x02\x12\x0e\n\x06remain\x18\x06 \x01(\x02\x12.\n\nevent_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"|\n\x12MovideoUserNewInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66irebase_id\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x31\n\rregister_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc4\x03\n\x1aMovideoVideoGenerationInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08video_id\x18\x02 \x01(\t\x12=\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32+.wati.ai_platform.protocol.movideo.CATEGORY\x12\x43\n\x0borientation\x18\x04 \x01(\x0e\x32..wati.ai_platform.protocol.movideo.ORIENTATION\x12\x13\n\x0buser_prompt\x18\x05 \x01(\t\x12\x12\n\nvoice_name\x18\x06 \x01(\t\x12\x14\n\x0chas_subtitle\x18\x07 \x01(\x08\x12\x10\n\x08\x64uration\x18\x08 \x01(\x05\x12<\n\x06status\x18\t \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12\x12\n\nerror_info\x18\n \x01(\t\x12.\n\nstart_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbe\x02\n\x16MovideoVideoExportInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08video_id\x18\x02 \x01(\t\x12:\n\x07quality\x18\x03 \x01(\x0e\x32).wati.ai_platform.protocol.common.QUALITY\x12<\n\x06status\x18\x04 \x01(\x0e\x32,.wati.ai_platform.protocol.common.TASKSTATUS\x12\x12\n\nerror_info\x18\x05 \x01(\t\x12\x15\n\rtarget_object\x18\x06 \x01(\t\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdd\x01\n\x13MovideoFeedbackInfo\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12\x10\n\x08video_id\x18\x02 \x01(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x15\n\rfeedback_type\x18\x04 \x01(\t\x12\x45\n\x0cis_favourite\x18\x05 \x01(\x0e\x32/.wati.ai_platform.protocol.common.USERFAVOURITE\x12\x31\n\rfeedback_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9a\x02\n\x17MovideoSubscriptionInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x02 \x01(\t\x12\x38\n\x04plan\x18\x03 \x01(\x0e\x32*.wati.ai_platform.protocol.common.USERTYPE\x12\x15\n\rcredit_before\x18\x04 \x01(\x05\x12\x14\n\x0c\x63redit_after\x18\x05 \x01(\x05\x12\x10\n\x08is_renew\x18\x06 \x01(\x08\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa4\x01\n\x12MovideoCreditUsage\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08video_id\x18\x02 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x03 \x01(\t\x12\x15\n\rcredit_before\x18\x04 \x01(\x05\x12\x0c\n\x04\x63ost\x18\x05 \x01(\x05\x12-\n\tcost_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa7\x01\n\x19MovideoSubscriptionCancel\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x38\n\x04plan\x18\x02 \x01(\x0e\x32*.wati.ai_platform.protocol.common.USERTYPE\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12/\n\x0b\x63\x61ncel_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf3\x0b\n\x11PushMetricRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x30.wati.ai_platform.protocol.metrics_server.ACTION\x12\x13\n\x0bis_finished\x18\x03 \x01(\x08\x12<\n\x05table\x18\x04 \x01(\x0e\x32-.wati.ai_platform.protocol.common.METRICTABLE\x12T\n\x0e\x63ommi_user_new\x18\x05 \x01(\x0b\x32:.wati.ai_platform.protocol.metrics_server.CommiUserNewInfoH\x00\x12Z\n\x11\x63ommi_user_active\x18\x06 \x01(\x0b\x32=.wati.ai_platform.protocol.metrics_server.CommiUserActiveInfoH\x00\x12\x62\n\x14\x63ommi_video_generate\x18\x07 \x01(\x0b\x32\x42.wati.ai_platform.protocol.metrics_server.CommiVideoGenerationInfoH\x00\x12[\n\x10\x63ommi_api_action\x18\x08 \x01(\x0b\x32?.wati.ai_platform.protocol.metrics_server.CommiAPIKeyActionInfoH\x00\x12V\n\x0f\x63ommi_api_usage\x18\t \x01(\x0b\x32;.wati.ai_platform.protocol.metrics_server.CommiAPIUsageInfoH\x00\x12Z\n\x11\x63ommi_video_share\x18\n \x01(\x0b\x32=.wati.ai_platform.protocol.metrics_server.CommiVideoShareInfoH\x00\x12\\\n\x12\x63ommi_credit_event\x18\x0b \x01(\x0b\x32>.wati.ai_platform.protocol.metrics_server.CommiCreditEventInfoH\x00\x12X\n\x10movideo_user_new\x18\x0c \x01(\x0b\x32<.wati.ai_platform.protocol.metrics_server.MovideoUserNewInfoH\x00\x12\x66\n\x16movideo_video_generate\x18\r \x01(\x0b\x32\x44.wati.ai_platform.protocol.metrics_server.MovideoVideoGenerationInfoH\x00\x12`\n\x14movideo_video_export\x18\x0e \x01(\x0b\x32@.wati.ai_platform.protocol.metrics_server.MovideoVideoExportInfoH\x00\x12Y\n\x10movideo_feedback\x18\x0f \x01(\x0b\x32=.wati.ai_platform.protocol.metrics_server.MovideoFeedbackInfoH\x00\x12\x61\n\x14movideo_subscription\x18\x10 \x01(\x0b\x32\x41.wati.ai_platform.protocol.metrics_server.MovideoSubscriptionInfoH\x00\x12\\\n\x14movideo_credit_usage\x18\x11 \x01(\x0b\x32<.wati.ai_platform.protocol.metrics_server.MovideoCreditUsageH\x00\x12j\n\x1bmovideo_subscription_cancel\x18\x12 \x01(\x0b\x32\x43.wati.ai_platform.protocol.metrics_server.MovideoSubscriptionCancelH\x00\x42\x0c\n\ntable_data\"\x14\n\x12PushMetricResponse\"\x14\n\x12HealthCheckRequest\"\x15\n\x13HealthCheckResponse**\n\x06\x41\x43TION\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06UPLOAD\x10\x02\x32\x99\x01\n\rMetricsServer\x12\x87\x01\n\nPushMetric\x12;.wati.ai_platform.protocol.metrics_server.PushMetricRequest\x1a<.wati.ai_platform.protocol.metrics_server.PushMetricResponseBYZ:github.com/ClareAI/ai-platform-protocol/api/metrics-server\x92\x41\x1a\x12\x18\n\x0fMetrics Service2\x05\x31.0.0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metrics_server.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z:github.com/ClareAI/ai-platform-protocol/api/metrics-server\222A\032\022\030\n\017Metrics Service2\0051.0.0'
  _globals['_COMMIVIDEOGENERATIONINFO_SCRIPTVARIABLESENTRY']._loaded_options = None
  _globals['_COMMIVIDEOGENERATIONINFO_SCRIPTVARIABLESENTRY']._serialized_options = b'8\001'
  _globals['_ACTION']._serialized_start=5620
  _globals['_ACTION']._serialized_end=5662
  _globals['_COMMIUSERNEWINFO']._serialized_start=205
  _globals['_COMMIUSERNEWINFO']._serialized_end=289
  _globals['_COMMIUSERACTIVEINFO']._serialized_start=292
  _globals['_COMMIUSERACTIVEINFO']._serialized_end=547
  _globals['_COMMIVIDEOGENERATIONINFO']._serialized_start=550
  _globals['_COMMIVIDEOGENERATIONINFO']._serialized_end=1359
  _globals['_COMMIVIDEOGENERATIONINFO_SCRIPTVARIABLESENTRY']._serialized_start=1305
  _globals['_COMMIVIDEOGENERATIONINFO_SCRIPTVARIABLESENTRY']._serialized_end=1359
  _globals['_COMMIAPIKEYACTIONINFO']._serialized_start=1362
  _globals['_COMMIAPIKEYACTIONINFO']._serialized_end=1550
  _globals['_COMMIAPIUSAGEINFO']._serialized_start=1553
  _globals['_COMMIAPIUSAGEINFO']._serialized_end=1741
  _globals['_COMMIVIDEOSHAREINFO']._serialized_start=1744
  _globals['_COMMIVIDEOSHAREINFO']._serialized_end=2003
  _globals['_COMMICREDITEVENTINFO']._serialized_start=2006
  _globals['_COMMICREDITEVENTINFO']._serialized_end=2277
  _globals['_MOVIDEOUSERNEWINFO']._serialized_start=2279
  _globals['_MOVIDEOUSERNEWINFO']._serialized_end=2403
  _globals['_MOVIDEOVIDEOGENERATIONINFO']._serialized_start=2406
  _globals['_MOVIDEOVIDEOGENERATIONINFO']._serialized_end=2858
  _globals['_MOVIDEOVIDEOEXPORTINFO']._serialized_start=2861
  _globals['_MOVIDEOVIDEOEXPORTINFO']._serialized_end=3179
  _globals['_MOVIDEOFEEDBACKINFO']._serialized_start=3182
  _globals['_MOVIDEOFEEDBACKINFO']._serialized_end=3403
  _globals['_MOVIDEOSUBSCRIPTIONINFO']._serialized_start=3406
  _globals['_MOVIDEOSUBSCRIPTIONINFO']._serialized_end=3688
  _globals['_MOVIDEOCREDITUSAGE']._serialized_start=3691
  _globals['_MOVIDEOCREDITUSAGE']._serialized_end=3855
  _globals['_MOVIDEOSUBSCRIPTIONCANCEL']._serialized_start=3858
  _globals['_MOVIDEOSUBSCRIPTIONCANCEL']._serialized_end=4025
  _globals['_PUSHMETRICREQUEST']._serialized_start=4028
  _globals['_PUSHMETRICREQUEST']._serialized_end=5551
  _globals['_PUSHMETRICRESPONSE']._serialized_start=5553
  _globals['_PUSHMETRICRESPONSE']._serialized_end=5573
  _globals['_HEALTHCHECKREQUEST']._serialized_start=5575
  _globals['_HEALTHCHECKREQUEST']._serialized_end=5595
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=5597
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=5618
  _globals['_METRICSSERVER']._serialized_start=5665
  _globals['_METRICSSERVER']._serialized_end=5818
# @@protoc_insertion_point(module_scope)
