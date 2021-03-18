{%- if cookiecutter.build_automation == "make" -%}
.PHONY: install format release clean clean-build clean-release clean-beet

DIST_DIR = dist
BUILD_DIR = build

{%- if cookiecutter.use_poetry == "y" %}
install:
	poetry lock -n
	poetry install -n
	poetry run pre-commit install
{% endif %}

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