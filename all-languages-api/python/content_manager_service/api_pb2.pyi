from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
import common_pb2 as _common_pb2
import commi_pb2 as _commi_pb2
import movideo_pb2 as _movideo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommiTemplateListRequest(_message.Message):
    __slots__ = ("user_id", "paging", "category", "name", "favourite")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    paging: _common_pb2.RequestPaging
    category: _commi_pb2.CATEGORY
    name: _common_pb2.NameQuery
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_id: _Optional[str] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class CommiTemplateListResponse(_message.Message):
    __slots__ = ("templates", "paging")
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[_commi_pb2.Template]
    paging: _common_pb2.ResponsePaging
    def __init__(self, templates: _Optional[_Iterable[_Union[_commi_pb2.Template, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class CommiTemplateGetRequest(_message.Message):
    __slots__ = ("user_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiTemplateGetResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _commi_pb2.Template
    def __init__(self, template: _Optional[_Union[_commi_pb2.Template, _Mapping]] = ...) -> None: ...

class CommiTemplateNewRequest(_message.Message):
    __slots__ = ("user_id", "name", "description", "category", "tags", "thumbnail")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    description: str
    category: _commi_pb2.CATEGORY
    tags: _containers.RepeatedScalarFieldContainer[str]
    thumbnail: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., tags: _Optional[_Iterable[str]] = ..., thumbnail: _Optional[str] = ...) -> None: ...

class CommiTemplateNewResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _commi_pb2.Template
    def __init__(self, template: _Optional[_Union[_commi_pb2.Template, _Mapping]] = ...) -> None: ...

class CommiTemplateUpdateRequest(_message.Message):
    __slots__ = ("user_id", "id", "name", "description", "tags", "thumbnail", "favourite")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    thumbnail: str
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., thumbnail: _Optional[str] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class CommiTemplateUpdateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _commi_pb2.Template
    def __init__(self, template: _Optional[_Union[_commi_pb2.Template, _Mapping]] = ...) -> None: ...

class CommiTemplateDeleteRequest(_message.Message):
    __slots__ = ("user_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiTemplateDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiTemplateScriptListRequest(_message.Message):
    __slots__ = ("user_id", "template_id", "paging")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    template_id: str
    paging: _common_pb2.RequestPaging
    def __init__(self, user_id: _Optional[str] = ..., template_id: _Optional[str] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class CommiTemplateScriptListResponse(_message.Message):
    __slots__ = ("scripts", "paging")
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    scripts: _containers.RepeatedCompositeFieldContainer[_commi_pb2.TemplateScript]
    paging: _common_pb2.ResponsePaging
    def __init__(self, scripts: _Optional[_Iterable[_Union[_commi_pb2.TemplateScript, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class CommiTemplateScriptGetRequest(_message.Message):
    __slots__ = ("user_id", "template_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    template_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., template_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiTemplateScriptGetResponse(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _commi_pb2.TemplateScript
    def __init__(self, script: _Optional[_Union[_commi_pb2.TemplateScript, _Mapping]] = ...) -> None: ...

class CommiTemplateScriptNewRequest(_message.Message):
    __slots__ = ("user_id", "template_id", "content", "parameters")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    template_id: str
    content: str
    parameters: _containers.RepeatedCompositeFieldContainer[_commi_pb2.TemplateScriptParameter]
    def __init__(self, user_id: _Optional[str] = ..., template_id: _Optional[str] = ..., content: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_commi_pb2.TemplateScriptParameter, _Mapping]]] = ...) -> None: ...

class CommiTemplateScriptNewResponse(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _commi_pb2.TemplateScript
    def __init__(self, script: _Optional[_Union[_commi_pb2.TemplateScript, _Mapping]] = ...) -> None: ...

class CommiTemplateScriptUpdateRequest(_message.Message):
    __slots__ = ("user_id", "template_id", "id", "content", "parameters")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    template_id: str
    id: str
    content: str
    parameters: _containers.RepeatedCompositeFieldContainer[_commi_pb2.TemplateScriptParameter]
    def __init__(self, user_id: _Optional[str] = ..., template_id: _Optional[str] = ..., id: _Optional[str] = ..., content: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_commi_pb2.TemplateScriptParameter, _Mapping]]] = ...) -> None: ...

class CommiTemplateScriptUpdateResponse(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _commi_pb2.TemplateScript
    def __init__(self, script: _Optional[_Union[_commi_pb2.TemplateScript, _Mapping]] = ...) -> None: ...

class CommiTemplateScriptDeleteRequest(_message.Message):
    __slots__ = ("user_id", "template_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    template_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., template_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiTemplateScriptDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiSpeakerListRequest(_message.Message):
    __slots__ = ("user_id", "paging", "name", "language", "favourite")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    paging: _common_pb2.RequestPaging
    name: _common_pb2.NameQuery
    language: _commi_pb2.LANGUAGE
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_id: _Optional[str] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., language: _Optional[_Union[_commi_pb2.LANGUAGE, str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class CommiSpeakerListResponse(_message.Message):
    __slots__ = ("speakers", "paging")
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    speakers: _containers.RepeatedCompositeFieldContainer[_commi_pb2.Speaker]
    paging: _common_pb2.ResponsePaging
    def __init__(self, speakers: _Optional[_Iterable[_Union[_commi_pb2.Speaker, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class CommiSpeakerGetRequest(_message.Message):
    __slots__ = ("user_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiSpeakerGetResponse(_message.Message):
    __slots__ = ("speaker",)
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    speaker: _commi_pb2.Speaker
    def __init__(self, speaker: _Optional[_Union[_commi_pb2.Speaker, _Mapping]] = ...) -> None: ...

class Avatar(_message.Message):
    __slots__ = ("thumbnail_name", "sample_video_name")
    THUMBNAIL_NAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_VIDEO_NAME_FIELD_NUMBER: _ClassVar[int]
    thumbnail_name: str
    sample_video_name: str
    def __init__(self, thumbnail_name: _Optional[str] = ..., sample_video_name: _Optional[str] = ...) -> None: ...

class CommiSpeakerNewRequest(_message.Message):
    __slots__ = ("user_id", "name", "language", "gender", "sample_audio_name", "default_avatar", "default_tone")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AVATAR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TONE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    language: _commi_pb2.LANGUAGE
    gender: _common_pb2.GENDER
    sample_audio_name: str
    default_avatar: Avatar
    default_tone: _common_pb2.TONE
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., language: _Optional[_Union[_commi_pb2.LANGUAGE, str]] = ..., gender: _Optional[_Union[_common_pb2.GENDER, str]] = ..., sample_audio_name: _Optional[str] = ..., default_avatar: _Optional[_Union[Avatar, _Mapping]] = ..., default_tone: _Optional[_Union[_common_pb2.TONE, str]] = ...) -> None: ...

class CommiSpeakerNewResponse(_message.Message):
    __slots__ = ("speaker",)
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    speaker: _commi_pb2.Speaker
    def __init__(self, speaker: _Optional[_Union[_commi_pb2.Speaker, _Mapping]] = ...) -> None: ...

class CommiSpeakerUpdateRequest(_message.Message):
    __slots__ = ("user_id", "id", "default_tone", "favourite")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TONE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    default_tone: _common_pb2.TONE
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ..., default_tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class CommiSpeakerUpdateResponse(_message.Message):
    __slots__ = ("speaker",)
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    speaker: _commi_pb2.Speaker
    def __init__(self, speaker: _Optional[_Union[_commi_pb2.Speaker, _Mapping]] = ...) -> None: ...

class CommiSpeakerDeleteRequest(_message.Message):
    __slots__ = ("user_id", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiSpeakerDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiUserVideoListRequest(_message.Message):
    __slots__ = ("user_id", "status", "is_ascending", "category", "name", "paging")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_ASCENDING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    status: _common_pb2.TASKSTATUS
    is_ascending: bool
    category: _commi_pb2.CATEGORY
    name: _common_pb2.NameQuery
    paging: _common_pb2.RequestPaging
    def __init__(self, user_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., is_ascending: bool = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., name: _Optional[_Union[_common_pb2.NameQuery, _Mapping]] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class CommiUserVideoListResponse(_message.Message):
    __slots__ = ("videos", "paging")
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    videos: _containers.RepeatedCompositeFieldContainer[_commi_pb2.Video]
    paging: _common_pb2.ResponsePaging
    def __init__(self, videos: _Optional[_Iterable[_Union[_commi_pb2.Video, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class CommiUserVideoNewTaskRequest(_message.Message):
    __slots__ = ("user_id", "name", "description", "template_id", "script_id", "script_parameter", "speaker_id", "tone", "result_callback_url", "source")
    class ScriptParameterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    RESULT_CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    description: str
    template_id: str
    script_id: str
    script_parameter: _containers.ScalarMap[str, str]
    speaker_id: str
    tone: _common_pb2.TONE
    result_callback_url: str
    source: _common_pb2.TASKSOURCE
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., template_id: _Optional[str] = ..., script_id: _Optional[str] = ..., script_parameter: _Optional[_Mapping[str, str]] = ..., speaker_id: _Optional[str] = ..., tone: _Optional[_Union[_common_pb2.TONE, str]] = ..., result_callback_url: _Optional[str] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ...) -> None: ...

class CommiUserVideoNewTaskResponse(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _common_pb2.TASKSTATUS
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ...) -> None: ...

class CommiUserVideoTaskStatusGetRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class CommiUserVideoTaskStatusGetResponse(_message.Message):
    __slots__ = ("status", "message", "estimated_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.TASKSTATUS
    message: str
    estimated_time: int
    def __init__(self, status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., message: _Optional[str] = ..., estimated_time: _Optional[int] = ...) -> None: ...

class CommiUserVideoGetRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class CommiUserVideoGetResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: _commi_pb2.Video
    def __init__(self, video: _Optional[_Union[_commi_pb2.Video, _Mapping]] = ...) -> None: ...

class CommiUserVideoUpdateRequest(_message.Message):
    __slots__ = ("user_id", "video_id", "name", "description")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    name: str
    description: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CommiUserVideoUpdateResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: _commi_pb2.Video
    def __init__(self, video: _Optional[_Union[_commi_pb2.Video, _Mapping]] = ...) -> None: ...

class CommiUserVideoDeleteRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class CommiUserVideoDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiUserVideoGenerationUsageListRequest(_message.Message):
    __slots__ = ("user_id", "source", "time_range")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    source: _common_pb2.TASKSOURCE
    time_range: _common_pb2.TimeRange
    def __init__(self, user_id: _Optional[str] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ...) -> None: ...

class CommiUserVideoGenerationUsageListResponse(_message.Message):
    __slots__ = ("usages",)
    USAGES_FIELD_NUMBER: _ClassVar[int]
    usages: _containers.RepeatedCompositeFieldContainer[_commi_pb2.VideoGenerationUsage]
    def __init__(self, usages: _Optional[_Iterable[_Union[_commi_pb2.VideoGenerationUsage, _Mapping]]] = ...) -> None: ...

class CommiSendWATIMessageRequest(_message.Message):
    __slots__ = ("user_id", "endpoint", "access_token", "broadcast_name", "template_name", "variable_name", "receivers")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECEIVERS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    endpoint: str
    access_token: str
    broadcast_name: str
    template_name: str
    variable_name: str
    receivers: _containers.RepeatedCompositeFieldContainer[_common_pb2.WatiReceiver]
    def __init__(self, user_id: _Optional[str] = ..., endpoint: _Optional[str] = ..., access_token: _Optional[str] = ..., broadcast_name: _Optional[str] = ..., template_name: _Optional[str] = ..., variable_name: _Optional[str] = ..., receivers: _Optional[_Iterable[_Union[_common_pb2.WatiReceiver, _Mapping]]] = ...) -> None: ...

class CommiSendWATIMessageResponse(_message.Message):
    __slots__ = ("rets",)
    RETS_FIELD_NUMBER: _ClassVar[int]
    rets: _containers.RepeatedCompositeFieldContainer[_common_pb2.Result]
    def __init__(self, rets: _Optional[_Iterable[_Union[_common_pb2.Result, _Mapping]]] = ...) -> None: ...

class CommiSpeakerSampleVideoGetRequest(_message.Message):
    __slots__ = ("user_id", "id", "template_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    id: str
    template_id: str
    def __init__(self, user_id: _Optional[str] = ..., id: _Optional[str] = ..., template_id: _Optional[str] = ...) -> None: ...

class CommiSpeakerSampleVideoGetResponse(_message.Message):
    __slots__ = ("sample_video_address",)
    SAMPLE_VIDEO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    sample_video_address: str
    def __init__(self, sample_video_address: _Optional[str] = ...) -> None: ...

class CommiUserVideoGetShareUrlRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class CommiUserVideoGetShareUrlResponse(_message.Message):
    __slots__ = ("share_url",)
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    share_url: str
    def __init__(self, share_url: _Optional[str] = ...) -> None: ...

class MovideoVoiceListRequest(_message.Message):
    __slots__ = ("user_id", "gender", "language", "paging")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    gender: _common_pb2.GENDER
    language: _movideo_pb2.LANGUAGE
    paging: _common_pb2.RequestPaging
    def __init__(self, user_id: _Optional[str] = ..., gender: _Optional[_Union[_common_pb2.GENDER, str]] = ..., language: _Optional[_Union[_movideo_pb2.LANGUAGE, str]] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class MovideoVoiceListResponse(_message.Message):
    __slots__ = ("voices", "paging")
    VOICES_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    voices: _containers.RepeatedCompositeFieldContainer[_movideo_pb2.Voice]
    paging: _common_pb2.ResponsePaging
    def __init__(self, voices: _Optional[_Iterable[_Union[_movideo_pb2.Voice, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class MovideoVoiceGetRequest(_message.Message):
    __slots__ = ("user_id", "name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class MovideoVoiceGetResponse(_message.Message):
    __slots__ = ("voice",)
    VOICE_FIELD_NUMBER: _ClassVar[int]
    voice: _movideo_pb2.Voice
    def __init__(self, voice: _Optional[_Union[_movideo_pb2.Voice, _Mapping]] = ...) -> None: ...

class MovideoUserListVideoRequest(_message.Message):
    __slots__ = ("user_id", "paging")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    paging: _common_pb2.RequestPaging
    def __init__(self, user_id: _Optional[str] = ..., paging: _Optional[_Union[_common_pb2.RequestPaging, _Mapping]] = ...) -> None: ...

class MovideoUserListVideoResponse(_message.Message):
    __slots__ = ("videos", "paging")
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    videos: _containers.RepeatedCompositeFieldContainer[_movideo_pb2.Video]
    paging: _common_pb2.ResponsePaging
    def __init__(self, videos: _Optional[_Iterable[_Union[_movideo_pb2.Video, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.ResponsePaging, _Mapping]] = ...) -> None: ...

class MovideoUserNewVideoTaskRequest(_message.Message):
    __slots__ = ("user_id", "orientation", "category", "outline", "voice", "duration", "add_subtitle")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    OUTLINE_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ADD_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    orientation: _movideo_pb2.ORIENTATION
    category: _movideo_pb2.CATEGORY
    outline: str
    voice: str
    duration: int
    add_subtitle: bool
    def __init__(self, user_id: _Optional[str] = ..., orientation: _Optional[_Union[_movideo_pb2.ORIENTATION, str]] = ..., category: _Optional[_Union[_movideo_pb2.CATEGORY, str]] = ..., outline: _Optional[str] = ..., voice: _Optional[str] = ..., duration: _Optional[int] = ..., add_subtitle: bool = ...) -> None: ...

class MovideoUserNewVideoTaskResponse(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _common_pb2.TASKSTATUS
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ...) -> None: ...

class MovideoUserTaskStatusGetRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class MovideoUserTaskStatusGetResponse(_message.Message):
    __slots__ = ("status", "message", "estimated_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.TASKSTATUS
    message: str
    estimated_time: int
    def __init__(self, status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., message: _Optional[str] = ..., estimated_time: _Optional[int] = ...) -> None: ...

class MovideoUserGetVideoRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class MovideoUserGetVideoResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: _movideo_pb2.Video
    def __init__(self, video: _Optional[_Union[_movideo_pb2.Video, _Mapping]] = ...) -> None: ...

class MovideoUserVideoExportTaskNewRequest(_message.Message):
    __slots__ = ("user_id", "video_id", "quality", "watermark")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    quality: _common_pb2.QUALITY
    watermark: _common_pb2.WATERMARK
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., quality: _Optional[_Union[_common_pb2.QUALITY, str]] = ..., watermark: _Optional[_Union[_common_pb2.WATERMARK, str]] = ...) -> None: ...

class MovideoUserVideoExportTaskNewResponse(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class MovideoUserVideoExportTaskGetRequest(_message.Message):
    __slots__ = ("user_id", "task_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    task_id: str
    def __init__(self, user_id: _Optional[str] = ..., task_id: _Optional[str] = ...) -> None: ...

class MovideoUserVideoExportTaskGetResponse(_message.Message):
    __slots__ = ("ret", "message", "video_address")
    RET_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ret: _common_pb2.TASKSTATUS
    message: str
    video_address: str
    def __init__(self, ret: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., message: _Optional[str] = ..., video_address: _Optional[str] = ...) -> None: ...

class MovideoUserUpdateVideoRequest(_message.Message):
    __slots__ = ("user_id", "video_id", "title", "favourite")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    title: str
    favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., title: _Optional[str] = ..., favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class MovideoUserUpdateVideoResponse(_message.Message):
    __slots__ = ("video",)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: _movideo_pb2.Video
    def __init__(self, video: _Optional[_Union[_movideo_pb2.Video, _Mapping]] = ...) -> None: ...

class MovideoUserDeleteVideoRequest(_message.Message):
    __slots__ = ("user_id", "video_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class MovideoUserDeleteVideoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoSendFeedBackRequest(_message.Message):
    __slots__ = ("user_email", "video_id", "comment", "feedback_type", "is_favourite")
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    user_email: str
    video_id: str
    comment: str
    feedback_type: str
    is_favourite: _common_pb2.USERFAVOURITE
    def __init__(self, user_email: _Optional[str] = ..., video_id: _Optional[str] = ..., comment: _Optional[str] = ..., feedback_type: _Optional[str] = ..., is_favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ...) -> None: ...

class MovideoSendFeedBackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
