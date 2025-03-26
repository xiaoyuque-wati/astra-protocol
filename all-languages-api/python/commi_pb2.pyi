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
    ALL: _ClassVar[CATEGORY]
    COMMERCE: _ClassVar[CATEGORY]
    MARKETING: _ClassVar[CATEGORY]
    PERSONAL_MESSAGE: _ClassVar[CATEGORY]

class LANGUAGE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANGUAGE_UNKNOWN: _ClassVar[LANGUAGE]
    EN_GB: _ClassVar[LANGUAGE]
    EN_US: _ClassVar[LANGUAGE]
    EN_IN: _ClassVar[LANGUAGE]
ALL: CATEGORY
COMMERCE: CATEGORY
MARKETING: CATEGORY
PERSONAL_MESSAGE: CATEGORY
LANGUAGE_UNKNOWN: LANGUAGE
EN_GB: LANGUAGE
EN_US: LANGUAGE
EN_IN: LANGUAGE

class Template(_message.Message):
    __slots__ = ("id", "name", "description", "category", "tags", "thumbnail_url", "default_speaker", "favourite", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SPEAKER_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    category: CATEGORY
    tags: _containers.RepeatedScalarFieldContainer[str]
    thumbnail_url: str
    default_speaker: str
    favourite: _common_pb2.USERFAVOURITE
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., category: _Optional[_Union[CATEGORY, str]] = ..., tags: _Optional[_Iterable[str]] = ..., thumbnail_url: _Optional[str] = ..., default_speaker: _Optional[str] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Speaker(_message.Message):
    __slots__ = ("id", "name", "language", "gender", "audio_sample", "avatar_image", "tone", "favourite", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_IMAGE_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    language: LANGUAGE
    gender: _common_pb2.GENDER
    audio_sample: str
    avatar_image: str
    tone: _common_pb2.TONE
    favourite: _common_pb2.USERFAVOURITE
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., language: _Optional[_Union[LANGUAGE, str]] = ..., gender: _Optional[_Union[_common_pb2.GENDER, str]] = ..., audio_sample: _Optional[str] = ..., avatar_image: _Optional[str] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Video(_message.Message):
    __slots__ = ("id", "name", "description", "video_url", "thumbnail_url", "duration", "category", "template_id", "speaker_id", "script_id", "script_parameter", "tone", "status", "create_at", "update_at")
    class ScriptParameterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    video_url: str
    thumbnail_url: str
    duration: int
    category: CATEGORY
    template_id: str
    speaker_id: str
    script_id: str
    script_parameter: _containers.ScalarMap[str, str]
    tone: _common_pb2.TONE
    status: _common_pb2.TASKSTATUS
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., video_url: _Optional[str] = ..., thumbnail_url: _Optional[str] = ..., duration: _Optional[int] = ..., category: _Optional[_Union[CATEGORY, str]] = ..., template_id: _Optional[str] = ..., speaker_id: _Optional[str] = ..., script_id: _Optional[str] = ..., script_parameter: _Optional[_Mapping[str, str]] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TemplateScriptParameter(_message.Message):
    __slots__ = ("key", "default_value", "is_required")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    key: str
    default_value: str
    is_required: bool
    def __init__(self, key: _Optional[str] = ..., default_value: _Optional[str] = ..., is_required: bool = ...) -> None: ...

class TemplateScript(_message.Message):
    __slots__ = ("id", "name", "content", "parameters", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    content: str
    parameters: _containers.RepeatedCompositeFieldContainer[TemplateScriptParameter]
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., content: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[TemplateScriptParameter, _Mapping]]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VideoGenerateRequest(_message.Message):
    __slots__ = ("video_id", "template", "values", "speaker_id", "language", "tone")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    template: str
    values: _containers.ScalarMap[str, str]
    speaker_id: str
    language: LANGUAGE
    tone: _common_pb2.TONE
    def __init__(self, video_id: _Optional[str] = ..., template: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., speaker_id: _Optional[str] = ..., language: _Optional[_Union[LANGUAGE, str]] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ...) -> None: ...

class VideoGenerateResult(_message.Message):
    __slots__ = ("video_id", "status", "error_info", "eta", "object", "duration", "word_count")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    WORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    status: _common_pb2.TASKSTATUS
    error_info: str
    eta: int
    object: str
    duration: int
    word_count: int
    def __init__(self, video_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., error_info: _Optional[str] = ..., eta: _Optional[int] = ..., object: _Optional[str] = ..., duration: _Optional[int] = ..., word_count: _Optional[int] = ...) -> None: ...

class VideoGenerationUsage(_message.Message):
    __slots__ = ("date", "total", "fail", "source")
    DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    total: int
    fail: int
    source: _common_pb2.TASKSOURCE
    def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total: _Optional[int] = ..., fail: _Optional[int] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ...) -> None: ...

class CreditInfo(_message.Message):
    __slots__ = ("credit",)
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    credit: float
    def __init__(self, credit: _Optional[float] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("id", "name", "email", "phone", "location", "language", "source", "type", "information", "credits", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    CREDITS_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    phone: str
    location: str
    language: str
    source: _common_pb2.USERSOURCE
    type: _common_pb2.USERTYPE
    information: str
    credits: CreditInfo
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., location: _Optional[str] = ..., language: _Optional[str] = ..., source: _Optional[_Union[_common_pb2.USERSOURCE, str]] = ..., type: _Optional[_Union[_common_pb2.USERTYPE, str]] = ..., information: _Optional[str] = ..., credits: _Optional[_Union[CreditInfo, _Mapping]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class APIKeyInfo(_message.Message):
    __slots__ = ("id", "sensitive_id", "name", "created_at", "last_used_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    sensitive_id: str
    name: str
    created_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., sensitive_id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreditUsage(_message.Message):
    __slots__ = ("date", "total_credits", "fail_credits", "source")
    DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CREDITS_FIELD_NUMBER: _ClassVar[int]
    FAIL_CREDITS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    total_credits: float
    fail_credits: float
    source: _common_pb2.TASKSOURCE
    def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_credits: _Optional[float] = ..., fail_credits: _Optional[float] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ...) -> None: ...
