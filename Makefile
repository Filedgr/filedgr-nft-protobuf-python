PROJECT_NAME = filedgr_nft_protobuf
DATE    ?= $(shell date +%FT%T%z)
MIN = 90

PYTHON = python
V = 0
Q = $(if $(filter 1,$V),,@)
M = $(shell printf "\033[34;1m▶\033[0m")

.PHONY: coverage
coverage:  ## test coverage package
	pip install -e .  > /dev/null && pip install pytest pytest-cov > /dev/null && sleep 1
	python -m pytest tests --cov=$(PROJECT_NAME) --cov-fail-under=$(MIN) --cov-report term-missing

.PHONY: lint
lint:
	pip install -e .  > /dev/null && pip install flake8 > /dev/null
	python -m flake8 src/$(PROJECT_NAME)

.PHONY: help
help:
	@grep -E '^[ a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'