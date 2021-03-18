{%- if cookiecutter.build_automation == "make" -%}
.PHONY: format release

DIST_DIR = dist
BUILD_DIR = build

format:
	black . --config pyproject.toml
	isort . --settings-path pyproject.toml

release:
	beet --config beet-release.json

clean: clean-build clean-release clean-beet

clean-build:
	rm -fr BUILD_DIR

clean-release:
	rm -fr DIST_DIR

clean-beet:
	beet cache --clear
{%- endif -%}