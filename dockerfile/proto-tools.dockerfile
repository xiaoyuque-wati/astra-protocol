FROM python:3.10-bullseye
ARG ARCH
ARG DEP
ARG PBVER=3.19.4
ARG GOVER=1.21.12

RUN apt-get -y update && apt-get -y upgrade

# install go
RUN wget -O go.tgz "https://go.dev/dl/go${GOVER}.linux-${ARCH}.tar.gz"; \
    tar -C /usr/local -xzf go.tgz && rm go.tgz

ENV GOPATH /go
ENV PATH $PATH:$GOPATH/bin:/usr/local/go/bin:

# install protoc
RUN set -eux; \
    \
    case "${ARCH}" in \
    amd64) arch='x86_64';; \
    arm64) arch='aarch_64';; \
    esac; \
    \
    PROTOC_ZIP="protoc-${PBVER}-linux-${arch}.zip"; \
    mkdir /tempprotoc && cd /tempprotoc; \
    curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v{$PBVER}/$PROTOC_ZIP; \
    unzip -o $PROTOC_ZIP -d /usr/local bin/protoc; \
    unzip -o $PROTOC_ZIP -d /usr/local 'include/*'; \
    rm -rf /tempprotoc;

RUN mkdir -p $GOPATH/src/github.com \
    && cd $GOPATH/src/github.com \
    && git clone https://github.com/googleapis/googleapis.git

COPY $DEP /dep
RUN cd /dep && go mod tidy \
        && go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway \
                      github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2 \
                      google.golang.org/protobuf/cmd/protoc-gen-go \
                      google.golang.org/grpc/cmd/protoc-gen-go-grpc \
                      github.com/envoyproxy/protoc-gen-validate;

RUN cd /dep && go install ./plugins/protoc-gen-api-paths.go
RUN rm -rf dep

RUN mkdir /grpc-gateway && curl -L https://github.com/grpc-ecosystem/grpc-gateway/archive/refs/tags/v2.19.1.tar.gz | \
    tar xvz --strip-components=1 -C /grpc-gateway
RUN pip install grpcio grpcio-tools protoc-gen-openapiv2 googleapis-common-protos
