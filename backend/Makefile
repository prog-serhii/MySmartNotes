libs := foundation graph text_ocr main web_app

define install_dev
	pip install -e $(1)

endef

.PHONY: dev
dev:
	pip install --use-feature=2020-resolver -r requirements.txt -r requirements-dev.txt
	$(foreach lib,$(libs),$(call install_dev,$(lib)))

.PHONY: freeze-deps
freeze-deps:
	pip install pip-tools==5.3.1
	pip-compile --upgrade --output-file=requirements.txt $(foreach lib,$(libs), ./$(lib)/requirements.txt ./$(lib)/requirements-dev.txt)