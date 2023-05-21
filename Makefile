all: build install

build:
	poetry build

install:
	poetry install

lint: format
	# stop the build if there are Python syntax errors or undefined names
	flake8 py_dmidecode --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 py_dmidecode --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black --check --line-length 127 .

fix:
	black --line-length 127 .

release: clean build
	poetry publish

clean:
	rm -fr  dist

.PHONY: all build install lint fix release clean