from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import commi_pb2 as _commi_pb2
import movideo_pb2 as _movideo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommiLoginAndRegisterRequest(_message.Message):
    __slots__ = ("source", "login_type", "email", "password", "extra_info")
    class LOGINTYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CommiLoginAndRegisterRequest.LOGINTYPE]
        PASSWORD: _ClassVar[CommiLoginAndRegisterRequest.LOGINTYPE]
        REGISTER: _ClassVar[CommiLoginAndRegisterRequest.LOGINTYPE]
        FORGET_PASSWORD: _ClassVar[CommiLoginAndRegisterRequest.LOGINTYPE]
    UNKNOWN: CommiLoginAndRegisterRequest.LOGINTYPE
    PASSWORD: CommiLoginAndRegisterRequest.LOGINTYPE
    REGISTER: CommiLoginAndRegisterRequest.LOGINTYPE
    FORGET_PASSWORD: CommiLoginAndRegisterRequest.LOGINTYPE
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    source: _common_pb2.USERSOURCE
    login_type: CommiLoginAndRegisterRequest.LOGINTYPE
    email: str
    password: str
    extra_info: str
    def __init__(self, source: _Optional[_Union[_common_pb2.USERSOURCE, str]] = ..., login_type: _Optional[_Union[CommiLoginAndRegisterRequest.LOGINTYPE, str]] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., extra_info: _Optional[str] = ...) -> None: ...

class CommiLoginAndRegisterResponse(_message.Message):
    __slots__ = ("user_id", "auth", "redirect_url")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    auth: str
    redirect_url: str
    def __init__(self, user_id: _Optional[str] = ..., auth: _Optional[str] = ..., redirect_url: _Optional[str] = ...) -> None: ...

class CommiResetPasswordRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class CommiResetPasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiUserActiveRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class CommiUserActiveResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiLogoutRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CommiLogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommiUserGetRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CommiUserGetResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _commi_pb2.UserInfo
    def __init__(self, user: _Optional[_Union[_commi_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class CommiUserUpdateRequest(_message.Message):
    __slots__ = ("user_id", "name", "password", "phone", "location", "langeuage", "information")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LANGEUAGE_FIELD_NUMBER: _ClassVar[int]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    password: str
    phone: str
    location: str
    langeuage: str
    information: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ..., phone: _Optional[str] = ..., location: _Optional[str] = ..., langeuage: _Optional[str] = ..., information: _Optional[str] = ...) -> None: ...

class CommiUserUpdateResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _commi_pb2.UserInfo
    def __init__(self, user: _Optional[_Union[_commi_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class UserAuthRequest(_message.Message):
    __slots__ = ("type", "auth")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    type: _common_pb2.AUTHTYPE
    auth: str
    def __init__(self, type: _Optional[_Union[_common_pb2.AUTHTYPE, str]] = ..., auth: _Optional[str] = ...) -> None: ...

class UserAuthResponse(_message.Message):
    __slots__ = ("user_id", "type", "product")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    type: _common_pb2.USERTYPE
    product: _common_pb2.PRODUCT
    def __init__(self, user_id: _Optional[str] = ..., type: _Optional[_Union[_common_pb2.USERTYPE, str]] = ..., product: _Optional[_Union[_common_pb2.PRODUCT, str]] = ...) -> None: ...

class CommiUserAPIKeyActionRequest(_message.Message):
    __slots__ = ("user_id", "action", "name", "id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    action: _common_pb2.APIKEYACTION
    name: str
    id: str
    def __init__(self, user_id: _Optional[str] = ..., action: _Optional[_Union[_common_pb2.APIKEYACTION, str]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CommiUserAPIKeyActionResponse(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: _commi_pb2.APIKeyInfo
    def __init__(self, api_key: _Optional[_Union[_commi_pb2.APIKeyInfo, _Mapping]] = ...) -> None: ...

class CommiUserAPIKeyListRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CommiUserAPIKeyListResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_commi_pb2.APIKeyInfo]
    def __init__(self, keys: _Optional[_Iterable[_Union[_commi_pb2.APIKeyInfo, _Mapping]]] = ...) -> None: ...

class CommiUserCreditUsageListRequest(_message.Message):
    __slots__ = ("user_id", "source", "range")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    source: _common_pb2.TASKSOURCE
    range: _common_pb2.TimeRange
    def __init__(self, user_id: _Optional[str] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ..., range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ...) -> None: ...

class CommiUserCreditUsageListResponse(_message.Message):
    __slots__ = ("usages",)
    USAGES_FIELD_NUMBER: _ClassVar[int]
    usages: _containers.RepeatedCompositeFieldContainer[_commi_pb2.CreditUsage]
    def __init__(self, usages: _Optional[_Iterable[_Union[_commi_pb2.CreditUsage, _Mapping]]] = ...) -> None: ...

class CommiBatchUsersAddCreditsRequest(_message.Message):
    __slots__ = ("user_emails", "credits", "expire_at")
    USER_EMAILS_FIELD_NUMBER: _ClassVar[int]
    CREDITS_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    user_emails: _containers.RepeatedScalarFieldContainer[str]
    credits: int
    expire_at: _timestamp_pb2.Timestamp
    def __init__(self, user_emails: _Optional[_Iterable[str]] = ..., credits: _Optional[int] = ..., expire_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommiBatchUsersAddCreditsResponse(_message.Message):
    __slots__ = ("rets",)
    RETS_FIELD_NUMBER: _ClassVar[int]
    rets: _containers.RepeatedCompositeFieldContainer[_common_pb2.Result]
    def __init__(self, rets: _Optional[_Iterable[_Union[_common_pb2.Result, _Mapping]]] = ...) -> None: ...

class CommiUserTaskCreditCostRequest(_message.Message):
    __slots__ = ("user_id", "item_id", "cost", "eta", "status", "source")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    item_id: str
    cost: int
    eta: int
    status: _common_pb2.TASKSTATUS
    source: _common_pb2.TASKSOURCE
    def __init__(self, user_id: _Optional[str] = ..., item_id: _Optional[str] = ..., cost: _Optional[int] = ..., eta: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ..., source: _Optional[_Union[_common_pb2.TASKSOURCE, str]] = ...) -> None: ...

class CommiUserTaskCreditCostResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserVerifyTokenRequest(_message.Message):
    __slots__ = ("id_token",)
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    def __init__(self, id_token: _Optional[str] = ...) -> None: ...

class MovideoUserVerifyTokenResponse(_message.Message):
    __slots__ = ("user_id", "token", "is_new_user")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_USER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    is_new_user: bool
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ..., is_new_user: bool = ...) -> None: ...

class MovideoUserLogoutRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserLogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserGetRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserGetResponse(_message.Message):
    __slots__ = ("user_info",)
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    user_info: _movideo_pb2.UserInfo
    def __init__(self, user_info: _Optional[_Union[_movideo_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class MovideoUserUpgradeRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserUpgradeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserGetUsageRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserGetUsageResponse(_message.Message):
    __slots__ = ("usage", "total")
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    usage: int
    total: int
    def __init__(self, usage: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class MovideoUserBalanceCostRequest(_message.Message):
    __slots__ = ("user_id", "item_id", "cost", "status")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    item_id: str
    cost: int
    status: _common_pb2.TASKSTATUS
    def __init__(self, user_id: _Optional[str] = ..., item_id: _Optional[str] = ..., cost: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.TASKSTATUS, str]] = ...) -> None: ...

class MovideoUserBalanceCostResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserDeleteRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserNewSubscriptionRequest(_message.Message):
    __slots__ = ("user_id", "rc_customer_id", "purchase_at", "event", "plan")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RC_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_AT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    rc_customer_id: str
    purchase_at: _timestamp_pb2.Timestamp
    event: _common_pb2.SUBSCRIPTION_EVENT
    plan: _common_pb2.USERTYPE
    def __init__(self, user_id: _Optional[str] = ..., rc_customer_id: _Optional[str] = ..., purchase_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event: _Optional[_Union[_common_pb2.SUBSCRIPTION_EVENT, str]] = ..., plan: _Optional[_Union[_common_pb2.USERTYPE, str]] = ...) -> None: ...

class MovideoUserNewSubscriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MovideoUserListSubscriptionsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class MovideoUserListSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_movideo_pb2.SubscriptionInfo]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_movideo_pb2.SubscriptionInfo, _Mapping]]] = ...) -> None: ...

class MovideoUserGetSubscriptionRequest(_message.Message):
    __slots__ = ("user_id", "subscription_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class MovideoUserGetSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _movideo_pb2.SubscriptionInfo
    def __init__(self, subscription: _Optional[_Union[_movideo_pb2.SubscriptionInfo, _Mapping]] = ...) -> None: ...

class MovideoSubscriptionEventRequest(_message.Message):
    __slots__ = ("event_message",)
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    event_message: str
    def __init__(self, event_message: _Optional[str] = ...) -> None: ...

class MovideoSubscriptionEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
