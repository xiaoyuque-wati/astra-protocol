from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import commi_pb2 as _commi_pb2
from . import movideo_pb2 as _movideo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ITEMTYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSUPPORT_ITEM: _ClassVar[ITEMTYPE]
    COMMI_VIDEO_GENERATE: _ClassVar[ITEMTYPE]
    MOVIDEO_VIDEO_GENERATE: _ClassVar[ITEMTYPE]
    MOVIDEO_VIDEO_EXPORT: _ClassVar[ITEMTYPE]
    IMAGE_GENERATOR: _ClassVar[ITEMTYPE]
UNSUPPORT_ITEM: ITEMTYPE
COMMI_VIDEO_GENERATE: ITEMTYPE
MOVIDEO_VIDEO_GENERATE: ITEMTYPE
MOVIDEO_VIDEO_EXPORT: ITEMTYPE
IMAGE_GENERATOR: ITEMTYPE

class ItemTaskRequest(_message.Message):
    __slots__ = ("id", "create_time", "item_type", "commi_video_generate", "movideo_video_generate", "movideo_video_export")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMI_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_EXPORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    create_time: _timestamp_pb2.Timestamp
    item_type: ITEMTYPE
    commi_video_generate: _commi_pb2.VideoGenerateRequest
    movideo_video_generate: _movideo_pb2.VideoGenerateRequest
    movideo_video_export: _movideo_pb2.VideoExportRequest
    def __init__(self, id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., item_type: _Optional[_Union[ITEMTYPE, str]] = ..., commi_video_generate: _Optional[_Union[_commi_pb2.VideoGenerateRequest, _Mapping]] = ..., movideo_video_generate: _Optional[_Union[_movideo_pb2.VideoGenerateRequest, _Mapping]] = ..., movideo_video_export: _Optional[_Union[_movideo_pb2.VideoExportRequest, _Mapping]] = ...) -> None: ...

class ItemTaskResponse(_message.Message):
    __slots__ = ("id", "item_type", "commi_video_generate", "movideo_video_generate", "movideo_video_export")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMI_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_EXPORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    item_type: ITEMTYPE
    commi_video_generate: _commi_pb2.VideoGenerateResult
    movideo_video_generate: _movideo_pb2.VideoGenerateResult
    movideo_video_export: _movideo_pb2.VideoExportResult
    def __init__(self, id: _Optional[str] = ..., item_type: _Optional[_Union[ITEMTYPE, str]] = ..., commi_video_generate: _Optional[_Union[_commi_pb2.VideoGenerateResult, _Mapping]] = ..., movideo_video_generate: _Optional[_Union[_movideo_pb2.VideoGenerateResult, _Mapping]] = ..., movideo_video_export: _Optional[_Union[_movideo_pb2.VideoExportResult, _Mapping]] = ...) -> None: ...
