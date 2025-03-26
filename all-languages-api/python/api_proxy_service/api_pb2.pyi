from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import commi_pb2 as _commi_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoTemplateListRequest(_message.Message):
    __slots__ = ("paging", "category", "name", "favourite")
    PAGING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    paging: _common_pb2.RequestPaging
    category: _commi_pb2.CATEGORY
    name: _common_pb2.NameQuery
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class Script(_message.Message):
    __slots__ = ("content", "parameters")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    content: str
    parameters: _containers.RepeatedCompositeFieldContainer[_commi_pb2.TemplateScriptParameter]
    def __init__(self, content: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_commi_pb2.TemplateScriptParameter, _Mapping]]] = ...) -> None: ...

class Template(_message.Message):
    __slots__ = ("id", "name", "description", "category", "tags", "favourite", "script", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    category: _commi_pb2.CATEGORY
    tags: _containers.RepeatedScalarFieldContainer[str]
    favourite: _common_pb2.USERFAVOURITE
    script: Script
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., tags: _Optional[_Iterable[str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., script: _Optional[_Union[Script, _Mapping]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VideoTemplateListResponse(_message.Message):
    __slots__ = ("templates", "paging")
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[Template]
    paging: _common_pb2.ResponsePaging
    def __init__(self, templates: _Optional[_Iterable[_Union[Template, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class VideoTemplateGetRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class VideoTemplateGetResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: Template
    def __init__(self, template: _Optional[_Union[Template, _Mapping]] = ...) -> None: ...

class VideoTemplateScriptListRequest(_message.Message):
    __slots__ = ("template_id", "paging")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    paging: _common_pb2.RequestPaging
    def __init__(self, template_id: _Optional[str] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class VideoTemplateScriptListResponse(_message.Message):
    __slots__ = ("scripts", "paging")
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    scripts: _containers.RepeatedCompositeFieldContainer[_commi_pb2.TemplateScript]
    paging: _common_pb2.ResponsePaging
    def __init__(self, scripts: _Optional[_Iterable[_Union[_commi_pb2.TemplateScript, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class VideoTemplateScriptGetRequest(_message.Message):
    __slots__ = ("template_id", "script_id")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    script_id: str
    def __init__(self, template_id: _Optional[str] = ..., script_id: _Optional[str] = ...) -> None: ...

class VideoTemplateScriptGetResponse(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _commi_pb2.TemplateScript
    def __init__(self, script: _Optional[_Union[_commi_pb2.TemplateScript, _Mapping]] = ...) -> None: ...

class SpeakerListRequest(_message.Message):
    __slots__ = ("paging", "name", "language", "favourite")
    PAGING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    paging: _common_pb2.RequestPaging
    name: _common_pb2.NameQuery
    language: _commi_pb2.LANGUAGE
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., language: _Optional[_Union[_commi_pb2.LANGUAGE, str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class Speaker(_message.Message):
    __slots__ = ("id", "name", "language", "gender", "audio_sample_name", "tone", "favourite", "create_at", "update_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SAMPLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    language: _commi_pb2.LANGUAGE
    gender: _common_pb2.GENDER
    audio_sample_name: str
    tone: _common_pb2.TONE
    favourite: _common_pb2.USERFAVOURITE
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., language: _Optional[_Union[_commi_pb2.LANGUAGE, str]] = ..., gender: _Optional[_Union[_common_pb2.GENDER, str]] = ..., audio_sample_name: _Optional[str] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SpeakerListResponse(_message.Message):
    __slots__ = ("speakers", "paging")
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    speakers: _containers.RepeatedCompositeFieldContainer[Speaker]
    paging: _common_pb2.ResponsePaging
    def __init__(self, speakers: _Optional[_Iterable[_Union[Speaker, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class SpeakerGetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SpeakerGetResponse(_message.Message):
    __slots__ = ("speaker",)
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    def __init__(self, speaker: _Optional[_Union[Speaker, _Mapping]] = ...) -> None: ...

class Video(_message.Message):
    __slots__ = ("id", "name", "description", "video_url", "duration", "category", "template_id", "speaker_id", "script_parameter", "tone", "status", "create_at", "update_at")
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
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    video_url: str
    duration: int
    category: _commi_pb2.CATEGORY
    template_id: str
    speaker_id: str
    script_parameter: _containers.ScalarMap[str, str]
    tone: _common_pb2.TONE
    status: _common_pb2.TASKSTATUS
    create_at: _timestamp_pb2.Timestamp
    update_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., video_url: _Optional[str] = ..., duration: _Optional[int] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., template_id: _Optional[str] = ..., speaker_id: _Optional[str] = ..., script_parameter: _Optional[_Mapping[str, str]] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., create_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VideoListRequest(_message.Message):
    __slots__ = ("status", "is_ascending", "category", "name", "paging")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_ASCENDING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.TASKSTATUS
    is_ascending: bool
    category: _commi_pb2.CATEGORY
    name: _common_pb2.NameQuery
    paging: _common_pb2.RequestPaging
    def __init__(self, status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., is_ascending: bool = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class VideoListResponse(_message.Message):
    __slots__ = ("videos", "paging")
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    videos: _containers.RepeatedCompositeFieldContainer[Video]
    paging: _common_pb2.ResponsePaging
    def __init__(self, videos: _Optional[_Iterable[_Union[Video, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class VideoNewTaskRequest(_message.Message):
    __slots__ = ("name", "description", "template_id", "script_parameter", "speaker_id", "tone", "result_callback_url")
    class ScriptParameterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    RESULT_CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    template_id: str
    script_parameter: _containers.ScalarMap[str, str]
    speaker_id: str
    tone: _common_pb2.TONE
    result_callback_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., template_id: _Optional[str] = ..., script_parameter: _Optional[_Mapping[str, str]] = ..., speaker_id: _Optional[str] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., result_callback_url: _Optional[str] = ...) -> None: ...

class VideoNewTaskResponse(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _common_pb2.TASKSTATUS
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ...) -> None: ...

class VideoTaskStatusGetRequest(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class VideoTaskStatusGetResponse(_message.Message):
    __slots__ = ("status", "message", "estimated_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.TASKSTATUS
    message: str
    estimated_time: int
    def __init__(self, status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., message: _Optional[str] = ..., estimated_time: _Optional[int] = ...) -> None: ...

class VideoGetRequest(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class VideoGetResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: Video
    def __init__(self, video: _Optional[_Union[Video, _Mapping]] = ...) -> None: ...

class VideoUpdateRequest(_message.Message):
    __slots__ = ("video_id", "name", "description")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    name: str
    description: str
    def __init__(self, video_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class VideoUpdateResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: Video
    def __init__(self, video: _Optional[_Union[Video, _Mapping]] = ...) -> None: ...

class VideoDeleteRequest(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class VideoDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatiCustomParam(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SendWATIMessageRequest(_message.Message):
    __slots__ = ("endpoint", "access_token", "broadcast_name", "template_name", "variable_name", "receivers")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECEIVERS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    access_token: str
    broadcast_name: str
    template_name: str
    variable_name: str
    receivers: _containers.RepeatedCompositeFieldContainer[_common_pb2.WatiReceiver]
    def __init__(self, endpoint: _Optional[str] = ..., access_token: _Optional[str] = ..., broadcast_name: _Optional[str] = ..., template_name: _Optional[str] = ..., variable_name: _Optional[str] = ..., receivers: _Optional[_Iterable[_Union[_common_pb2.WatiReceiver, _Mapping]]] = ...) -> None: ...

class SendWATIMessageResponse(_message.Message):
    __slots__ = ("rets",)
    RETS_FIELD_NUMBER: _ClassVar[int]
    rets: _containers.RepeatedCompositeFieldContainer[_common_pb2.Result]
    def __init__(self, rets: _Optional[_Iterable[_Union[_common_pb2.Result, _Mapping]]] = ...) -> None: ...
