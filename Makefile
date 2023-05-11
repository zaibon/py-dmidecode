all: build install

build:
	poetry build

install:
	poetry install

release: clean
	poetry publish

clean:
	rm -fr  dist

.PHONY: all build install release clean