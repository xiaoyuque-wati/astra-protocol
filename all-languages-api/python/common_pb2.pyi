from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class USERFAVOURITE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAVOURITE_UNKNOWN: _ClassVar[USERFAVOURITE]
    UNFAVOURITE: _ClassVar[USERFAVOURITE]
    FAVOURITE: _ClassVar[USERFAVOURITE]

class USERTYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTYPE: _ClassVar[USERTYPE]
    FREE: _ClassVar[USERTYPE]
    CREATOR: _ClassVar[USERTYPE]
    PRO: _ClassVar[USERTYPE]

class GENDER(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[GENDER]
    MALE: _ClassVar[GENDER]
    FEMALE: _ClassVar[GENDER]

class TONE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL_TONE: _ClassVar[TONE]
    CONFIDENT: _ClassVar[TONE]
    FRIENDLY: _ClassVar[TONE]

class AUTHTYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[AUTHTYPE]
    TOKEN: _ClassVar[AUTHTYPE]
    API_KEY: _ClassVar[AUTHTYPE]

class USERSOURCE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSUPPORT: _ClassVar[USERSOURCE]
    REGISTER: _ClassVar[USERSOURCE]
    WATI: _ClassVar[USERSOURCE]
    GOOGLE: _ClassVar[USERSOURCE]
    APPLE: _ClassVar[USERSOURCE]

class APIKEYACTION(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[APIKEYACTION]
    CREATE: _ClassVar[APIKEYACTION]
    DELETE: _ClassVar[APIKEYACTION]
    GET: _ClassVar[APIKEYACTION]

class USERCREDITEVENT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_ACTION: _ClassVar[USERCREDITEVENT]
    ADD: _ClassVar[USERCREDITEVENT]
    MINUS: _ClassVar[USERCREDITEVENT]

class SUBSCRIPTION_STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_SUBSCRIPTION: _ClassVar[SUBSCRIPTION_STATUS]
    SUBSCRIBED: _ClassVar[SUBSCRIPTION_STATUS]
    SUBSCRIPTION_FAILED: _ClassVar[SUBSCRIPTION_STATUS]
    SUBSCRIPTION_EXPIRED: _ClassVar[SUBSCRIPTION_STATUS]

class SUBSCRIPTION_EVENT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_EVENT: _ClassVar[SUBSCRIPTION_EVENT]
    PURCHASE_PRODUCT: _ClassVar[SUBSCRIPTION_EVENT]
    CHANGE_PRODUCT: _ClassVar[SUBSCRIPTION_EVENT]

class STATUSCODE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SC_OK: _ClassVar[STATUSCODE]
    SC_CANCELLED: _ClassVar[STATUSCODE]
    SC_UNKNOWN: _ClassVar[STATUSCODE]
    SC_INVALID_ARGUMENT: _ClassVar[STATUSCODE]
    SC_DEADLINE_EXCEEDED: _ClassVar[STATUSCODE]
    SC_NOT_FOUND: _ClassVar[STATUSCODE]
    SC_ALREADY_EXISTS: _ClassVar[STATUSCODE]
    SC_PERMISSION_DENIED: _ClassVar[STATUSCODE]
    SC_UNAUTHENTICATED: _ClassVar[STATUSCODE]
    SC_RESOURCE_EXHAUSTED: _ClassVar[STATUSCODE]
    SC_FAILED_PRECONDITION: _ClassVar[STATUSCODE]
    SC_ABORTED: _ClassVar[STATUSCODE]
    SC_OUT_OF_RANGE: _ClassVar[STATUSCODE]
    SC_UNIMPLEMENTED: _ClassVar[STATUSCODE]
    SC_INTERNAL: _ClassVar[STATUSCODE]
    SC_UNAVAILABLE: _ClassVar[STATUSCODE]
    SC_DATA_LOSS: _ClassVar[STATUSCODE]

class QUALITY(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[QUALITY]
    PIXEL_480P: _ClassVar[QUALITY]
    PIXEL_720P: _ClassVar[QUALITY]
    PIXEL_1080P: _ClassVar[QUALITY]

class TASKSTATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_UNKNOWN: _ClassVar[TASKSTATUS]
    PENDING: _ClassVar[TASKSTATUS]
    PROCESSING: _ClassVar[TASKSTATUS]
    SUCCESS: _ClassVar[TASKSTATUS]
    FAILURE: _ClassVar[TASKSTATUS]

class WATERMARK(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_WM: _ClassVar[WATERMARK]
    NO_WM: _ClassVar[WATERMARK]
    WM_CUSTOM: _ClassVar[WATERMARK]
    WM_MOVIDEO: _ClassVar[WATERMARK]

class TASKSOURCE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_UNKNOWN: _ClassVar[TASKSOURCE]
    WEBUI: _ClassVar[TASKSOURCE]
    API: _ClassVar[TASKSOURCE]

class METRICTABLE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_UNDEFINED: _ClassVar[METRICTABLE]
    COMMI_USER_NEW: _ClassVar[METRICTABLE]
    COMMI_USER_ACTIVE: _ClassVar[METRICTABLE]
    COMMI_VIDEO_GENERATION: _ClassVar[METRICTABLE]
    COMMI_API_KEY_ACTION: _ClassVar[METRICTABLE]
    COMMI_API_USAGE: _ClassVar[METRICTABLE]
    COMMI_VIDEO_SHARE: _ClassVar[METRICTABLE]
    COMMI_CREDIT_EVENT: _ClassVar[METRICTABLE]
    MOVIDEO_USER_NEW: _ClassVar[METRICTABLE]
    MOVIDEO_VIDEO_GENERATION: _ClassVar[METRICTABLE]
    MOVIDEO_VIDEO_EXPORT: _ClassVar[METRICTABLE]
    MOVIDEO_FEEDBACK: _ClassVar[METRICTABLE]
    MOVIDEO_SUBSCRIPTION: _ClassVar[METRICTABLE]
    MOVIDEO_CREDIT_EVENT: _ClassVar[METRICTABLE]
    MOVIDEO_SUB_CANCELLATION: _ClassVar[METRICTABLE]

class PRODUCT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNKNOWN: _ClassVar[PRODUCT]
    COMMI: _ClassVar[PRODUCT]
    MOVIDEO: _ClassVar[PRODUCT]
FAVOURITE_UNKNOWN: USERFAVOURITE
UNFAVOURITE: USERFAVOURITE
FAVOURITE: USERFAVOURITE
NOTYPE: USERTYPE
FREE: USERTYPE
CREATOR: USERTYPE
PRO: USERTYPE
UNKNOWN: GENDER
MALE: GENDER
FEMALE: GENDER
ALL_TONE: TONE
CONFIDENT: TONE
FRIENDLY: TONE
INVALID: AUTHTYPE
TOKEN: AUTHTYPE
API_KEY: AUTHTYPE
UNSUPPORT: USERSOURCE
REGISTER: USERSOURCE
WATI: USERSOURCE
GOOGLE: USERSOURCE
APPLE: USERSOURCE
UNDEFINED: APIKEYACTION
CREATE: APIKEYACTION
DELETE: APIKEYACTION
GET: APIKEYACTION
NO_ACTION: USERCREDITEVENT
ADD: USERCREDITEVENT
MINUS: USERCREDITEVENT
NO_SUBSCRIPTION: SUBSCRIPTION_STATUS
SUBSCRIBED: SUBSCRIPTION_STATUS
SUBSCRIPTION_FAILED: SUBSCRIPTION_STATUS
SUBSCRIPTION_EXPIRED: SUBSCRIPTION_STATUS
NO_EVENT: SUBSCRIPTION_EVENT
PURCHASE_PRODUCT: SUBSCRIPTION_EVENT
CHANGE_PRODUCT: SUBSCRIPTION_EVENT
SC_OK: STATUSCODE
SC_CANCELLED: STATUSCODE
SC_UNKNOWN: STATUSCODE
SC_INVALID_ARGUMENT: STATUSCODE
SC_DEADLINE_EXCEEDED: STATUSCODE
SC_NOT_FOUND: STATUSCODE
SC_ALREADY_EXISTS: STATUSCODE
SC_PERMISSION_DENIED: STATUSCODE
SC_UNAUTHENTICATED: STATUSCODE
SC_RESOURCE_EXHAUSTED: STATUSCODE
SC_FAILED_PRECONDITION: STATUSCODE
SC_ABORTED: STATUSCODE
SC_OUT_OF_RANGE: STATUSCODE
SC_UNIMPLEMENTED: STATUSCODE
SC_INTERNAL: STATUSCODE
SC_UNAVAILABLE: STATUSCODE
SC_DATA_LOSS: STATUSCODE
UNSPECIFIED: QUALITY
PIXEL_480P: QUALITY
PIXEL_720P: QUALITY
PIXEL_1080P: QUALITY
TASK_UNKNOWN: TASKSTATUS
PENDING: TASKSTATUS
PROCESSING: TASKSTATUS
SUCCESS: TASKSTATUS
FAILURE: TASKSTATUS
UNKNOWN_WM: WATERMARK
NO_WM: WATERMARK
WM_CUSTOM: WATERMARK
WM_MOVIDEO: WATERMARK
SOURCE_UNKNOWN: TASKSOURCE
WEBUI: TASKSOURCE
API: TASKSOURCE
METRIC_UNDEFINED: METRICTABLE
COMMI_USER_NEW: METRICTABLE
COMMI_USER_ACTIVE: METRICTABLE
COMMI_VIDEO_GENERATION: METRICTABLE
COMMI_API_KEY_ACTION: METRICTABLE
COMMI_API_USAGE: METRICTABLE
COMMI_VIDEO_SHARE: METRICTABLE
COMMI_CREDIT_EVENT: METRICTABLE
MOVIDEO_USER_NEW: METRICTABLE
MOVIDEO_VIDEO_GENERATION: METRICTABLE
MOVIDEO_VIDEO_EXPORT: METRICTABLE
MOVIDEO_FEEDBACK: METRICTABLE
MOVIDEO_SUBSCRIPTION: METRICTABLE
MOVIDEO_CREDIT_EVENT: METRICTABLE
MOVIDEO_SUB_CANCELLATION: METRICTABLE
PRODUCT_UNKNOWN: PRODUCT
COMMI: PRODUCT
MOVIDEO: PRODUCT

class Result(_message.Message):
    __slots__ = ("code", "error", "status")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    code: int
    error: str
    status: STATUSCODE
    def __init__(self, code: _Optional[int] = ..., error: _Optional[str] = ..., status: _Optional[_Union[STATUSCODE, str]] = ...) -> None: ...

class ResponsePaging(_message.Message):
    __slots__ = ("offset", "limit", "total")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    total: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class RequestPaging(_message.Message):
    __slots__ = ("offset", "limit")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class NameQuery(_message.Message):
    __slots__ = ("value", "match_mode")
    class MATCHMODE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FUZZY: _ClassVar[NameQuery.MATCHMODE]
        EXACT: _ClassVar[NameQuery.MATCHMODE]
    FUZZY: NameQuery.MATCHMODE
    EXACT: NameQuery.MATCHMODE
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    value: str
    match_mode: NameQuery.MATCHMODE
    def __init__(self, value: _Optional[str] = ..., match_mode: _Optional[_Union[NameQuery.MATCHMODE, str]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WatiReceiver(_message.Message):
    __slots__ = ("whatsapp_number", "shared_item_id", "other_custom_params")
    class CustomParam(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WHATSAPP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SHARED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_CUSTOM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    whatsapp_number: str
    shared_item_id: str
    other_custom_params: _containers.RepeatedCompositeFieldContainer[WatiReceiver.CustomParam]
    def __init__(self, whatsapp_number: _Optional[str] = ..., shared_item_id: _Optional[str] = ..., other_custom_params: _Optional[_Iterable[_Union[WatiReceiver.CustomParam, _Mapping]]] = ...) -> None: ...
