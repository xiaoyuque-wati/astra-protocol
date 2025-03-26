## 简介

WATI-AIGC-PLATFORM 是 wati 内部的aigc产品相关的api文档

### 架构
![architecture](./architecture.png)

### 功能：

#### API-PROXY-SERVICE
对外代理服务, 负责对接口鉴权以及转发请求到对应的服务
语言: GOLANG

#### USER-MANAGER-SERVICE
用户管理服务, 负责管理用户/用户登录鉴权/用户credit相关功能
语言: GOLANG

#### CONTENT-MANAGER-SERVICE
内容管理服务, 负责对公共以及用户的资源进行管理, 包括生成/删除视频, 获取人像列表等等.
语言: GOLANG

#### MODEL-ADAPTER-SERVICE
负责对不同模型进行调用来生成视频或音频, 无API, 通过PUBSUB接收请求.
语言: PYTHON

#### METRICS-SERVICE
负责收集统计数据并上传到BigQuery.
语言: GOLANG

<!-- [Swagger](wati-aigc-openapi.swagger.json) | [Client](wati-aigc-openapi-generated.tar.gz) -->

## API通用惯例

### JSON编码规则

1. string子类型：
    * string(int64) 请求字段，可以传入数字或字符串表示的数字，若数字过大（2^31以上）受JSON Number的精度限制，建议传字符串形式
    * string(int64) 返回字段，为字符串类型的十进制数字形式，如"1000000"
    * string(byte)  请求/返回字段，传入Base64编码后的二进制数据，如"YWJjMTIzIT8kKiYoKSctPUB+"
    * string(date-time) 请求/返回字段，传入RFC 3339格式日期字符串，如"2017-01-01T10:00:20.021Z"
2. 请求字段缺失时，默认值规则：
    * string, 默认空字符串""
    * int32/int64/float，默认为0
    * bool，默认为false
    * object，默认为null
    * array，默认为空数组
3. 返回字段缺失，应按上述规则处理

### 错误码

1. 服务处理异常时，统一返回如下格式JSON： `{"code": 1, "message": "verbose error message"}`
2. 异常时返回HTTP错误代码及`code`字段意义如下：

|Code|缩写|HTTP错误码|解释|
|--- |--- |--- |--- |
|0|OK|200|成功|
|3|INVALID_ARGUMENT|400|无效参数|
|5|NOT_FOUND|404|资源未找到|
|6|ALREADY_EXISTS|409|资源已存在|
|7|PERMISSION_DENIED|403|非法访问|
|8|RESOURCE_EXHAUSTED|429|用户同时调用次数过多|
|9|FAILED_PRECONDITION|402|用户余额不足|
|12|UNIMPLEMENTED|501|未实现|
|13|INTERNAL|500|服务器内部错误|
|16|UNAUTHENTICATED|401|用户未验证/鉴权未通过|

### 接口鉴权
鉴权分为`API_KEY`和`TOKEN`

用户访问资源时调用时在 Authorization HTTP 头中包含 TOKEN/API_KEY，格式如下：
```
Authorization: Bearer [TOKEN/API_KEY]
```

