#!make
include common.mk
include custom.mk

.PHONY: help
## This help
help:
	@printf "Usage:\n";

	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9\/]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf "\033[36m%-25s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-\_0-9\/.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "\033[36m%-25s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = helpMessage"\n                           "substr($$0, 3); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n                          "helpMessage"\n" \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

## Develop

## Starts services
deploy:
	@cd $(GITROOT)/src && GOOGLE_APPLICATION_CREDENTIALS=service-account.json uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## -- Deployment --

## publish
publish:
	@gcloud --project $(PROJECT_ID) app deploy src/app.yaml src/cron.yaml

## -- CI --

## format check (dry run)
format-check:
	autoflake "$(GITROOT)/src" -r
	isort --diff "$(GITROOT)/src"
	black --check "$(GITROOT)/src"

## format
format:
	autoflake "$(GITROOT)/src" -r -i
	isort "$(GITROOT)/src"
	black "$(GITROOT)/src"

## linting
lint:
ifeq ($(CI), true)
	docker run --rm -v $(GITROOT):/app $(BASE_IMAGE) black --check .
else
	black --check src
endif
