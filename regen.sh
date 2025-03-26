#!/usr/bin/env bash
set -e

REPO_ROOT=${PWD}

PROJECT_NAME=github.com/ClareAI/ai-platform-protocol
GEN_DIR=${REPO_ROOT}/all-languages-api/

safeDelete() {
	if [ -d "$1" ]; then
		echo "remove existing directory: " $1
		rm -r $1
	fi
}

safeDelete ${GEN_DIR}
mkdir -p ${GEN_DIR}/go
mkdir -p ${GEN_DIR}/swagger
mkdir -p ${GEN_DIR}/python

PROTO_INCLUDE="-I$REPO_ROOT/pb "
PROTO_INCLUDE+="-I$PROTOC_INSTALL/include "
PROTO_INCLUDE+="-I$GOPATH/src/github.com/googleapis "
PROTO_INCLUDE+="-I$GOPATH/pkg/mod/github.com/grpc-ecosystem/grpc-gateway/v2@v2.19.1"

for i in $(find $(pwd)/ -name "*.proto" | grep -v thirdparty); do
	proto_file=$i
	echo "Process --- " ${proto_file}
	# go
	protoc ${PROTO_INCLUDE} \
		--go_out ${GEN_DIR}/go ${proto_file}
	# grpc
	protoc ${PROTO_INCLUDE} \
		--go-grpc_out ${GEN_DIR}/go ${proto_file}
	# grpc gateway
	protoc ${PROTO_INCLUDE} \
		--grpc-gateway_out=logtostderr=true:${GEN_DIR}/go \
		${proto_file}
	# --api-paths_out=${GEN_DIR}/go \

	# swagger
	protoc ${PROTO_INCLUDE} \
		--openapiv2_opt allow_patch_feature=true \
		--openapiv2_opt disable_default_errors=true \
		--openapiv2_opt logtostderr=true \
		--openapiv2_opt json_names_for_fields=false \
		--openapiv2_opt simple_operation_ids=true \
		--openapiv2_out=logtostderr=true:${GEN_DIR}/swagger ${proto_file}

	# python
	python -m grpc_tools.protoc ${PROTO_INCLUDE} \
		--python_out=${GEN_DIR}/python \
		--grpc_python_out=${GEN_DIR}/python \
		--pyi_out=${GEN_DIR}/python \
		${proto_file}
done

# copy golang api
safeDelete api
mv ${GEN_DIR}/go/${PROJECT_NAME}/api ./api/
rm -rf ${GEN_DIR}/go

echo "success!"
