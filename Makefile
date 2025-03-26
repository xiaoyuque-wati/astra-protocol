SRC = $(shell find pb -type f -name "*.proto")
ARCH = $(shell uname -m)

DOC_TAG = v0.0.1
DOC_IMAGE_NAME = wati-aigc-api-doc

IMAGE_TAG = v0.0.1
IMAGE_NAME = proto-tools:$(IMAGE_TAG)

OS := $(shell uname)
ifeq ($(OS),Darwin)
    OPEN_CMD := open
else ifeq ($(OS),Linux)
    OPEN_CMD := xdg-open
else
    OPEN_CMD := start
endif

.PHONY: image
image:
	@echo "build docker in architecture: $(ARCH)"
	docker build --build-arg ARCH=$(ARCH) --build-arg DEP=./dockerfile/dep -t $(IMAGE_NAME) -f ./dockerfile/proto-tools.dockerfile .


PROJECT_PATH := $(CURDIR)
PROJECT_NAME := $(notdir $(PROJECT_PATH))
PATH_IN_CONTAINER := /go/src/wati.io/aigc/$(PROJECT_NAME)

.PHONY: proto
proto:
	chmod +x ./regen.sh
	docker run -it --rm --entrypoint=bash -u root:root -v ${PROJECT_PATH}:${PATH_IN_CONTAINER} -e PROTOC_INSTALL=/usr/local -w ${PATH_IN_CONTAINER} $(IMAGE_NAME) ./regen.sh


.PHONY: doc
doc:
	@if ! docker image inspect $(DOC_IMAGE_NAME):$(DOC_TAG) >/dev/null 2>&1; then \
		echo "Image $(DOC_IMAGE_NAME):$(DOC_TAG) does not exist, building..."; \
		docker build -t $(DOC_IMAGE_NAME):$(DOC_TAG) -f dockerfile/doc-builder.dockerfile .; \
	fi

	@$(OPEN_CMD) http://localhost:8000 || echo "\033[33mPlease open http://localhost:8000 in your browser\033[0m"

	docker run --rm -p 8000:8000 --name $(DOC_IMAGE_NAME) $(DOC_IMAGE_NAME):$(DOC_TAG)


.PHONY: proto-fmt
proto-fmt:
	@echo "formatting proto files $(SRC)"
	@clang-format -i $(SRC)
	@if [ -n "$$(git status --porcelain 2>/dev/null)" ]; then \
		echo "$$(git status --porcelain $(SRC))"; \
		exit 1; \
	fi