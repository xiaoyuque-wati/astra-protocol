from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CATEGORY(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[CATEGORY]
    ADVERTISING: _ClassVar[CATEGORY]
    STORY_TELLING: _ClassVar[CATEGORY]
    INFORMATIVE: _ClassVar[CATEGORY]
    ENTERTAINING: _ClassVar[CATEGORY]
    PROFESSIONAL: _ClassVar[CATEGORY]
    INSPIRING: _ClassVar[CATEGORY]

class LANGUAGE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[LANGUAGE]
    ENGLISH: _ClassVar[LANGUAGE]
    PORTUGUESE: _ClassVar[LANGUAGE]

class ORIENTATION(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_SET: _ClassVar[ORIENTATION]
    PORTRAIT: _ClassVar[ORIENTATION]
    LANDSCAPE: _ClassVar[ORIENTATION]
UNDEFINED: CATEGORY
ADVERTISING: CATEGORY
STORY_TELLING: CATEGORY
INFORMATIVE: CATEGORY
ENTERTAINING: CATEGORY
PROFESSIONAL: CATEGORY
INSPIRING: CATEGORY
UNKNOWN: LANGUAGE
ENGLISH: LANGUAGE
PORTUGUESE: LANGUAGE
NOT_SET: ORIENTATION
PORTRAIT: ORIENTATION
LANDSCAPE: ORIENTATION

class Voice(_message.Message):
    __slots__ = ("name", "description", "language", "gender", "tags", "audio_demo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DEMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    language: LANGUAGE
    gender: _common_pb2.GENDER
    tags: _containers.RepeatedScalarFieldContainer[str]
    audio_demo: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., language: _Optional[_Union[LANGUAGE, str]] = ..., gender: _Optional[_Union[_common_pb2.GENDER, str]] = ..., tags: _Optional[_Iterable[str]] = ..., audio_demo: _Optional[str] = ...) -> None: ...

class VideoClip(_message.Message):
    __slots__ = ("index", "sentence", "clip_url", "audio_segment_url", "video_description")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SENTENCE_FIELD_NUMBER: _ClassVar[int]
    CLIP_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SEGMENT_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    index: int
    sentence: str
    clip_url: str
    audio_segment_url: str
    video_description: str
    def __init__(self, index: _Optional[int] = ..., sentence: _Optional[str] = ..., clip_url: _Optional[str] = ..., audio_segment_url: _Optional[str] = ..., video_description: _Optional[str] = ...) -> None: ...

class Video(_message.Message):
    __slots__ = ("id", "status", "title", "category", "source_content", "voice_name", "preview_video_url", "thumbnail_url", "duration", "voiceover_word_count", "clips", "favourite", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    VOICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    VOICEOVER_WORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLIPS_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _common_pb2.TASKSTATUS
    title: str
    category: CATEGORY
    source_content: str
    voice_name: str
    preview_video_url: str
    thumbnail_url: str
    duration: int
    voiceover_word_count: int
    clips: _containers.RepeatedCompositeFieldContainer[VideoClip]
    favourite: _common_pb2.USERFAVOURITE
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., title: _Optional[str] = ..., category: _Optional[_Union[CATEGORY, str]] = ..., source_content: _Optional[str] = ..., voice_name: _Optional[str] = ..., preview_video_url: _Optional[str] = ..., thumbnail_url: _Optional[str] = ..., duration: _Optional[int] = ..., voiceover_word_count: _Optional[int] = ..., clips: _Optional[_Iterable[_Union[VideoClip, _Mapping]]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VideoGenerateRequest(_message.Message):
    __slots__ = ("video_id", "category", "outline", "orientation", "voice_id", "language", "duration", "add_subtitle")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    OUTLINE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ADD_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    category: CATEGORY
    outline: str
    orientation: ORIENTATION
    voice_id: str
    language: LANGUAGE
    duration: int
    add_subtitle: bool
    def __init__(self, video_id: _Optional[str] = ..., category: _Optional[_Union[CATEGORY, str]] = ..., outline: _Optional[str] = ..., orientation: _Optional[_Union[ORIENTATION, str]] = ..., voice_id: _Optional[str] = ..., language: _Optional[_Union[LANGUAGE, str]] = ..., duration: _Optional[int] = ..., add_subtitle: bool = ...) -> None: ...

class VideoGenerateResult(_message.Message):
    __slots__ = ("video_id", "status", "error_info", "title", "preview_video", "thumbnail", "duration", "voiceover_word_count")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_VIDEO_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    VOICEOVER_WORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    status: _common_pb2.TASKSTATUS
    error_info: str
    title: str
    preview_video: str
    thumbnail: str
    duration: int
    voiceover_word_count: int
    def __init__(self, video_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., error_info: _Optional[str] = ..., title: _Optional[str] = ..., preview_video: _Optional[str] = ..., thumbnail: _Optional[str] = ..., duration: _Optional[int] = ..., voiceover_word_count: _Optional[int] = ...) -> None: ...

class VideoExportRequest(_message.Message):
    __slots__ = ("video_id", "quality", "watermark", "add_subtitle")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_FIELD_NUMBER: _ClassVar[int]
    ADD_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    quality: _common_pb2.QUALITY
    watermark: _common_pb2.WATERMARK
    add_subtitle: bool
    def __init__(self, video_id: _Optional[str] = ..., quality: _Optional[_Union[_common_pb2.QUALITY, str]] = ..., watermark: _Optional[_Union[_common_pb2.WATERMARK, str]] = ..., add_subtitle: bool = ...) -> None: ...

class VideoExportResult(_message.Message):
    __slots__ = ("video_id", "status", "error_info", "video_object")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OBJECT_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    status: _common_pb2.TASKSTATUS
    error_info: str
    video_object: str
    def __init__(self, video_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., error_info: _Optional[str] = ..., video_object: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("id", "email", "type", "subscribe_info", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    type: _common_pb2.USERTYPE
    subscribe_info: SubscriptionInfo
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., type: _Optional[_Union[_common_pb2.USERTYPE, str]] = ..., subscribe_info: _Optional[_Union[SubscriptionInfo, _Mapping]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubscriptionInfo(_message.Message):
    __slots__ = ("id", "status", "error_info", "start_at", "experation_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    EXPERATION_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _common_pb2.SUBSCRIPTION_STATUS
    error_info: str
    start_at: _timestamp_pb2.Timestamp
    experation_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.SUBSCRIPTION_STATUS, str]] = ..., error_info: _Optional[str] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., experation_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
