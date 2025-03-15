all: build install

build:
	uv build

test:
	uv run pytest --cov=dmidecode

test-ci:
	uv run pytest --cov=dmidecode --cov-report=xml

lint: format
	# stop the build if there are Python syntax errors or undefined names
	uv run flake8 dmidecode --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	uv run flake8 dmidecode --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	uv run black --check --line-length 127 .

fix:
	uv run black --line-length 127 .

release: clean build
	uv publish

clean:
	rm -fr  dist

.PHONY: all build install lint fix release clean