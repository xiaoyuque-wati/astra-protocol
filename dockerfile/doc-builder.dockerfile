FROM ruby:3.2-alpine

RUN apk add --no-cache nodejs npm \
    && npm install -g @redocly/cli serve

WORKDIR /app

COPY dockerfile/doc_dep/ /app
COPY all-languages-api/swagger/ /app/swagger

ENV SWAGGER_CODEGEN_CLI_JAR=/app/swagger-codegen-cli.jar

RUN chmod +x /app/regen_swagger.sh && \
    /app/regen_swagger.sh

COPY doc/architecture.png /app/generated/docs/

EXPOSE 8000

CMD ["serve", "-l", "8000", "generated/docs"]

