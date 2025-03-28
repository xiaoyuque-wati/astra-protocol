# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common.proto
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
    'common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12 wati.ai_platform.protocol.common\x1a\x1fgoogle/protobuf/timestamp.proto\"c\n\x06Result\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.wati.ai_platform.protocol.common.STATUSCODE\">\n\x0eResponsePaging\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\r\n\x05total\x18\x03 \x01(\x03\".\n\rRequestPaging\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\"\x88\x01\n\tNameQuery\x12\r\n\x05value\x18\x01 \x01(\t\x12I\n\nmatch_mode\x18\x02 \x01(\x0e\x32\x35.wati.ai_platform.protocol.common.NameQuery.MATCHMODE\"!\n\tMATCHMODE\x12\t\n\x05\x46UZZY\x10\x00\x12\t\n\x05\x45XACT\x10\x01\"_\n\tTimeRange\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc4\x01\n\x0cWatiReceiver\x12\x17\n\x0fwhatsapp_number\x18\x01 \x01(\t\x12\x16\n\x0eshared_item_id\x18\x02 \x01(\t\x12W\n\x13other_custom_params\x18\x03 \x03(\x0b\x32:.wati.ai_platform.protocol.common.WatiReceiver.CustomParam\x1a*\n\x0b\x43ustomParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t*F\n\rUSERFAVOURITE\x12\x15\n\x11\x46\x41VOURITE_UNKNOWN\x10\x00\x12\x0f\n\x0bUNFAVOURITE\x10\x01\x12\r\n\tFAVOURITE\x10\x02*6\n\x08USERTYPE\x12\n\n\x06NOTYPE\x10\x00\x12\x08\n\x04\x46REE\x10\x01\x12\x0b\n\x07\x43REATOR\x10\x02\x12\x07\n\x03PRO\x10\x03*+\n\x06GENDER\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02*1\n\x04TONE\x12\x0c\n\x08\x41LL_TONE\x10\x00\x12\r\n\tCONFIDENT\x10\x01\x12\x0c\n\x08\x46RIENDLY\x10\x02*/\n\x08\x41UTHTYPE\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05TOKEN\x10\x01\x12\x0b\n\x07\x41PI_KEY\x10\x02*J\n\nUSERSOURCE\x12\r\n\tUNSUPPORT\x10\x00\x12\x0c\n\x08REGISTER\x10\x01\x12\x08\n\x04WATI\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x12\t\n\x05\x41PPLE\x10\x04*>\n\x0c\x41PIKEYACTION\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x07\n\x03GET\x10\x03*4\n\x0fUSERCREDITEVENT\x12\r\n\tNO_ACTION\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\t\n\x05MINUS\x10\x02*m\n\x13SUBSCRIPTION_STATUS\x12\x13\n\x0fNO_SUBSCRIPTION\x10\x00\x12\x0e\n\nSUBSCRIBED\x10\n\x12\x17\n\x13SUBSCRIPTION_FAILED\x10\x14\x12\x18\n\x14SUBSCRIPTION_EXPIRED\x10\x1e*L\n\x12SUBSCRIPTION_EVENT\x12\x0c\n\x08NO_EVENT\x10\x00\x12\x14\n\x10PURCHASE_PRODUCT\x10\x01\x12\x12\n\x0e\x43HANGE_PRODUCT\x10\x02*\xf0\x02\n\nSTATUSCODE\x12\t\n\x05SC_OK\x10\x00\x12\x10\n\x0cSC_CANCELLED\x10\x01\x12\x0e\n\nSC_UNKNOWN\x10\x02\x12\x17\n\x13SC_INVALID_ARGUMENT\x10\x03\x12\x18\n\x14SC_DEADLINE_EXCEEDED\x10\x04\x12\x10\n\x0cSC_NOT_FOUND\x10\x05\x12\x15\n\x11SC_ALREADY_EXISTS\x10\x06\x12\x18\n\x14SC_PERMISSION_DENIED\x10\x07\x12\x16\n\x12SC_UNAUTHENTICATED\x10\x10\x12\x19\n\x15SC_RESOURCE_EXHAUSTED\x10\x08\x12\x1a\n\x16SC_FAILED_PRECONDITION\x10\t\x12\x0e\n\nSC_ABORTED\x10\n\x12\x13\n\x0fSC_OUT_OF_RANGE\x10\x0b\x12\x14\n\x10SC_UNIMPLEMENTED\x10\x0c\x12\x0f\n\x0bSC_INTERNAL\x10\r\x12\x12\n\x0eSC_UNAVAILABLE\x10\x0e\x12\x10\n\x0cSC_DATA_LOSS\x10\x0f*K\n\x07QUALITY\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nPIXEL_480P\x10\x01\x12\x0e\n\nPIXEL_720P\x10\x02\x12\x0f\n\x0bPIXEL_1080P\x10\x03*U\n\nTASKSTATUS\x12\x10\n\x0cTASK_UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\x0b\n\x07\x46\x41ILURE\x10\x04*E\n\tWATERMARK\x12\x0e\n\nUNKNOWN_WM\x10\x00\x12\t\n\x05NO_WM\x10\x01\x12\r\n\tWM_CUSTOM\x10\x02\x12\x0e\n\nWM_MOVIDEO\x10\x03*4\n\nTASKSOURCE\x12\x12\n\x0eSOURCE_UNKNOWN\x10\x00\x12\t\n\x05WEBUI\x10\x01\x12\x07\n\x03\x41PI\x10\x02*\xfe\x02\n\x0bMETRICTABLE\x12\x14\n\x10METRIC_UNDEFINED\x10\x00\x12\x12\n\x0e\x43OMMI_USER_NEW\x10\x01\x12\x15\n\x11\x43OMMI_USER_ACTIVE\x10\x02\x12\x1a\n\x16\x43OMMI_VIDEO_GENERATION\x10\x03\x12\x18\n\x14\x43OMMI_API_KEY_ACTION\x10\x04\x12\x13\n\x0f\x43OMMI_API_USAGE\x10\x05\x12\x15\n\x11\x43OMMI_VIDEO_SHARE\x10\x06\x12\x16\n\x12\x43OMMI_CREDIT_EVENT\x10\x07\x12\x14\n\x10MOVIDEO_USER_NEW\x10\x08\x12\x1c\n\x18MOVIDEO_VIDEO_GENERATION\x10\t\x12\x18\n\x14MOVIDEO_VIDEO_EXPORT\x10\n\x12\x14\n\x10MOVIDEO_FEEDBACK\x10\x0b\x12\x18\n\x14MOVIDEO_SUBSCRIPTION\x10\x0c\x12\x18\n\x14MOVIDEO_CREDIT_EVENT\x10\r\x12\x1c\n\x18MOVIDEO_SUB_CANCELLATION\x10\x0e*6\n\x07PRODUCT\x12\x13\n\x0fPRODUCT_UNKNOWN\x10\x00\x12\t\n\x05\x43OMMI\x10\x01\x12\x0b\n\x07MOVIDEO\x10\x02\x42\x34Z2github.com/ClareAI/ai-platform-protocol/api/commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/ClareAI/ai-platform-protocol/api/common'
  _globals['_USERFAVOURITE']._serialized_start=731
  _globals['_USERFAVOURITE']._serialized_end=801
  _globals['_USERTYPE']._serialized_start=803
  _globals['_USERTYPE']._serialized_end=857
  _globals['_GENDER']._serialized_start=859
  _globals['_GENDER']._serialized_end=902
  _globals['_TONE']._serialized_start=904
  _globals['_TONE']._serialized_end=953
  _globals['_AUTHTYPE']._serialized_start=955
  _globals['_AUTHTYPE']._serialized_end=1002
  _globals['_USERSOURCE']._serialized_start=1004
  _globals['_USERSOURCE']._serialized_end=1078
  _globals['_APIKEYACTION']._serialized_start=1080
  _globals['_APIKEYACTION']._serialized_end=1142
  _globals['_USERCREDITEVENT']._serialized_start=1144
  _globals['_USERCREDITEVENT']._serialized_end=1196
  _globals['_SUBSCRIPTION_STATUS']._serialized_start=1198
  _globals['_SUBSCRIPTION_STATUS']._serialized_end=1307
  _globals['_SUBSCRIPTION_EVENT']._serialized_start=1309
  _globals['_SUBSCRIPTION_EVENT']._serialized_end=1385
  _globals['_STATUSCODE']._serialized_start=1388
  _globals['_STATUSCODE']._serialized_end=1756
  _globals['_QUALITY']._serialized_start=1758
  _globals['_QUALITY']._serialized_end=1833
  _globals['_TASKSTATUS']._serialized_start=1835
  _globals['_TASKSTATUS']._serialized_end=1920
  _globals['_WATERMARK']._serialized_start=1922
  _globals['_WATERMARK']._serialized_end=1991
  _globals['_TASKSOURCE']._serialized_start=1993
  _globals['_TASKSOURCE']._serialized_end=2045
  _globals['_METRICTABLE']._serialized_start=2048
  _globals['_METRICTABLE']._serialized_end=2430
  _globals['_PRODUCT']._serialized_start=2432
  _globals['_PRODUCT']._serialized_end=2486
  _globals['_RESULT']._serialized_start=83
  _globals['_RESULT']._serialized_end=182
  _globals['_RESPONSEPAGING']._serialized_start=184
  _globals['_RESPONSEPAGING']._serialized_end=246
  _globals['_REQUESTPAGING']._serialized_start=248
  _globals['_REQUESTPAGING']._serialized_end=294
  _globals['_NAMEQUERY']._serialized_start=297
  _globals['_NAMEQUERY']._serialized_end=433
  _globals['_NAMEQUERY_MATCHMODE']._serialized_start=400
  _globals['_NAMEQUERY_MATCHMODE']._serialized_end=433
  _globals['_TIMERANGE']._serialized_start=435
  _globals['_TIMERANGE']._serialized_end=530
  _globals['_WATIRECEIVER']._serialized_start=533
  _globals['_WATIRECEIVER']._serialized_end=729
  _globals['_WATIRECEIVER_CUSTOMPARAM']._serialized_start=687
  _globals['_WATIRECEIVER_CUSTOMPARAM']._serialized_end=729
# @@protoc_insertion_point(module_scope)
