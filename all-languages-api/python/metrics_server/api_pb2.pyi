from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import commi_pb2 as _commi_pb2
import movideo_pb2 as _movideo_pb2
import task_pb2 as _task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ACTION(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ACTION]
    ADD: _ClassVar[ACTION]
    UPLOAD: _ClassVar[ACTION]
UNKNOWN: ACTION
ADD: ACTION
UPLOAD: ACTION

class CommiUserNewInfo(_message.Message):
    __slots__ = ("email", "register_time")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TIME_FIELD_NUMBER: _ClassVar[int]
    email: str
    register_time: _timestamp_pb2.Timestamp
    def __init__(self, email: _Optional[str] = ..., register_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiUserActiveInfo(_message.Message):
    __slots__ = ("email", "id", "name", "phone", "country", "information", "initial_credit", "source", "first_login_time")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CREDIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FIRST_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: str
    name: str
    phone: str
    country: str
    information: str
    initial_credit: float
    source: _common_pb2.USERSOURCE
    first_login_time: _timestamp_pb2.Timestamp
    def __init__(self, email: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., phone: _Optional[str] = ..., country: _Optional[str] = ..., information: _Optional[str] = ..., initial_credit: _Optional[float] = ..., source: _Optional[_Union[_common_pb2.USERSOURCE, str]] = ..., first_login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiVideoGenerationInfo(_message.Message):
    __slots__ = ("video_id", "video_name", "user_id", "start_time", "end_time", "interval", "result", "template_id", "template_name", "category", "speaker_id", "speaker_name", "language", "script_word_count", "template_script", "script", "script_variables", "video_duration", "source", "credit_cost")
    class ScriptVariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_WORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DURATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREDIT_COST_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    video_name: str
    user_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    interval: int
    result: _common_pb2.TASKSTATUS
    template_id: str
    template_name: str
    category: _commi_pb2.CATEGORY
    speaker_id: str
    speaker_name: str
    language: _commi_pb2.LANGUAGE
    script_word_count: int
    template_script: str
    script: str
    script_variables: _containers.ScalarMap[str, str]
    video_duration: int
    source: _common_pb2.TASKSOURCE
    credit_cost: float
    def __init__(self, video_id: _Optional[str] = ..., video_name: _Optional[str] = ..., user_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[int] = ..., result: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., template_id: _Optional[str] = ..., template_name: _Optional[str] = ..., category: _Optional[_Union[_commi_pb2.CATEGORY, str]] = ..., speaker_id: _Optional[str] = ..., speaker_name: _Optional[str] = ..., language: _Optional[_Union[_commi_pb2.LANGUAGE, str]] = ..., script_word_count: _Optional[int] = ..., template_script: _Optional[str] = ..., script: _Optional[str] = ..., script_variables: _Optional[_Mapping[str, str]] = ..., video_duration: _Optional[int] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ..., credit_cost: _Optional[float] = ...) -> None: ...

class CommiAPIKeyActionInfo(_message.Message):
    __slots__ = ("user_id", "api_key_id", "api_key_name", "action", "time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    api_key_id: str
    api_key_name: str
    action: _common_pb2.APIKEYACTION
    time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., api_key_name: _Optional[str] = ..., action: _Optional[_Union[_common_pb2.APIKEYACTION, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiAPIUsageInfo(_message.Message):
    __slots__ = ("user_id", "api_key_id", "endpoint", "method", "status_code", "status_message", "invocation_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    api_key_id: str
    endpoint: str
    method: str
    status_code: int
    status_message: str
    invocation_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., endpoint: _Optional[str] = ..., method: _Optional[str] = ..., status_code: _Optional[int] = ..., status_message: _Optional[str] = ..., invocation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiVideoShareInfo(_message.Message):
    __slots__ = ("user_id", "video_id", "video_url", "wati_template_name", "wati_broadcast_name", "whatsapp_number", "send_status_code", "send_status_message", "send_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    WATI_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    WATI_BROADCAST_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEND_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    SEND_STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    video_url: str
    wati_template_name: str
    wati_broadcast_name: str
    whatsapp_number: str
    send_status_code: int
    send_status_message: str
    send_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., video_url: _Optional[str] = ..., wati_template_name: _Optional[str] = ..., wati_broadcast_name: _Optional[str] = ..., whatsapp_number: _Optional[str] = ..., send_status_code: _Optional[int] = ..., send_status_message: _Optional[str] = ..., send_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiCreditEventInfo(_message.Message):
    __slots__ = ("user_id", "action", "item_type", "item_id", "change_amount", "remain", "event_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAIN_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    action: _common_pb2.USERCREDITEVENT
    item_type: _task_pb2.ITEMTYPE
    item_id: str
    change_amount: float
    remain: float
    event_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., action: _Optional[_Union[_common_pb2.USERCREDITEVENT, str]] = ..., item_type: _Optional[_Union[_task_pb2.ITEMTYPE, str]] = ..., item_id: _Optional[str] = ..., change_amount: _Optional[float] = ..., remain: _Optional[float] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoUserNewInfo(_message.Message):
    __slots__ = ("user_id", "firebase_id", "email", "register_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIREBASE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    firebase_id: str
    email: str
    register_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., firebase_id: _Optional[str] = ..., email: _Optional[str] = ..., register_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoVideoGenerationInfo(_message.Message):
    __slots__ = ("user_id", "video_id", "category", "orientation", "user_prompt", "voice_name", "has_subtitle", "duration", "status", "error_info", "start_time", "end_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    VOICE_NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    category: _movideo_pb2.CATEGORY
    orientation: _movideo_pb2.ORIENTATION
    user_prompt: str
    voice_name: str
    has_subtitle: bool
    duration: int
    status: _common_pb2.TASKSTATUS
    error_info: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., category: _Optional[_Union[_movideo_pb2.CATEGORY, str]] = ..., orientation: _Optional[_Union[_movideo_pb2.ORIENTATION, str]] = ..., user_prompt: _Optional[str] = ..., voice_name: _Optional[str] = ..., has_subtitle: bool = ..., duration: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., error_info: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoVideoExportInfo(_message.Message):
    __slots__ = ("user_id", "video_id", "quality", "status", "error_info", "target_object", "start_time", "end_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    TARGET_OBJECT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    quality: _common_pb2.QUALITY
    status: _common_pb2.TASKSTATUS
    error_info: str
    target_object: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., quality: _Optional[_Union[_common_pb2.QUALITY, str]] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., error_info: _Optional[str] = ..., target_object: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoFeedbackInfo(_message.Message):
    __slots__ = ("user_email", "video_id", "comment", "feedback_type", "is_favourite", "feedback_time")
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FAVOURITE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_TIME_FIELD_NUMBER: _ClassVar[int]
    user_email: str
    video_id: str
    comment: str
    feedback_type: str
    is_favourite: _common_pb2.USERFAVOURITE
    feedback_time: _timestamp_pb2.Timestamp
    def __init__(self, user_email: _Optional[str] = ..., video_id: _Optional[str] = ..., comment: _Optional[str] = ..., feedback_type: _Optional[str] = ..., is_favourite: _Optional[_Union[_common_pb2.USERFAVOURITE, str]] = ..., feedback_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoSubscriptionInfo(_message.Message):
    __slots__ = ("user_id", "subscription_id", "plan", "credit_before", "credit_after", "is_renew", "start_time", "end_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    CREDIT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    CREDIT_AFTER_FIELD_NUMBER: _ClassVar[int]
    IS_RENEW_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    plan: _common_pb2.USERTYPE
    credit_before: int
    credit_after: int
    is_renew: bool
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., plan: _Optional[_Union[_common_pb2.USERTYPE, str]] = ..., credit_before: _Optional[int] = ..., credit_after: _Optional[int] = ..., is_renew: bool = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoCreditUsage(_message.Message):
    __slots__ = ("user_id", "video_id", "subscription_id", "credit_before", "cost", "cost_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREDIT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    COST_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    video_id: str
    subscription_id: str
    credit_before: int
    cost: int
    cost_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., video_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., credit_before: _Optional[int] = ..., cost: _Optional[int] = ..., cost_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MovideoSubscriptionCancel(_message.Message):
    __slots__ = ("user_id", "plan", "reason", "cancel_time")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    plan: _common_pb2.USERTYPE
    reason: str
    cancel_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., plan: _Optional[_Union[_common_pb2.USERTYPE, str]] = ..., reason: _Optional[str] = ..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PushMetricRequest(_message.Message):
    __slots__ = ("id", "action", "is_finished", "table", "commi_user_new", "commi_user_active", "commi_video_generate", "commi_api_action", "commi_api_usage", "commi_video_share", "commi_credit_event", "movideo_user_new", "movideo_video_generate", "movideo_video_export", "movideo_feedback", "movideo_subscription", "movideo_credit_usage", "movideo_subscription_cancel")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COMMI_USER_NEW_FIELD_NUMBER: _ClassVar[int]
    COMMI_USER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    COMMI_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    COMMI_API_ACTION_FIELD_NUMBER: _ClassVar[int]
    COMMI_API_USAGE_FIELD_NUMBER: _ClassVar[int]
    COMMI_VIDEO_SHARE_FIELD_NUMBER: _ClassVar[int]
    COMMI_CREDIT_EVENT_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_USER_NEW_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_VIDEO_EXPORT_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_CREDIT_USAGE_FIELD_NUMBER: _ClassVar[int]
    MOVIDEO_SUBSCRIPTION_CANCEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: ACTION
    is_finished: bool
    table: _common_pb2.METRICTABLE
    commi_user_new: CommiUserNewInfo
    commi_user_active: CommiUserActiveInfo
    commi_video_generate: CommiVideoGenerationInfo
    commi_api_action: CommiAPIKeyActionInfo
    commi_api_usage: CommiAPIUsageInfo
    commi_video_share: CommiVideoShareInfo
    commi_credit_event: CommiCreditEventInfo
    movideo_user_new: MovideoUserNewInfo
    movideo_video_generate: MovideoVideoGenerationInfo
    movideo_video_export: MovideoVideoExportInfo
    movideo_feedback: MovideoFeedbackInfo
    movideo_subscription: MovideoSubscriptionInfo
    movideo_credit_usage: MovideoCreditUsage
    movideo_subscription_cancel: MovideoSubscriptionCancel
    def __init__(self, id: _Optional[str] = ..., action: _Optional[_Union[ACTION, str]] = ..., is_finished: bool = ..., table: _Optional[_Union[_common_pb2.METRICTABLE, str]] = ..., commi_user_new: _Optional[_Union[CommiUserNewInfo, _Mapping]] = ..., commi_user_active: _Optional[_Union[CommiUserActiveInfo, _Mapping]] = ..., commi_video_generate: _Optional[_Union[CommiVideoGenerationInfo, _Mapping]] = ..., commi_api_action: _Optional[_Union[CommiAPIKeyActionInfo, _Mapping]] = ..., commi_api_usage: _Optional[_Union[CommiAPIUsageInfo, _Mapping]] = ..., commi_video_share: _Optional[_Union[CommiVideoShareInfo, _Mapping]] = ..., commi_credit_event: _Optional[_Union[CommiCreditEventInfo, _Mapping]] = ..., movideo_user_new: _Optional[_Union[MovideoUserNewInfo, _Mapping]] = ..., movideo_video_generate: _Optional[_Union[MovideoVideoGenerationInfo, _Mapping]] = ..., movideo_video_export: _Optional[_Union[MovideoVideoExportInfo, _Mapping]] = ..., movideo_feedback: _Optional[_Union[MovideoFeedbackInfo, _Mapping]] = ..., movideo_subscription: _Optional[_Union[MovideoSubscriptionInfo, _Mapping]] = ..., movideo_credit_usage: _Optional[_Union[MovideoCreditUsage, _Mapping]] = ..., movideo_subscription_cancel: _Optional[_Union[MovideoSubscriptionCancel, _Mapping]] = ...) -> None: ...

class PushMetricResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthCheckRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthCheckResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
