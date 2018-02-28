all: build install

build:
	python setup.py build

install:
	python setup.py install

package: source_pkg bin_pkg

source_pkg:
	python3 setup.py sdist

bin_pkg:
	python3 setup.py bdist_wheel

release: clean package
	twine upload dist/*

clean:
	rm -fr build dist dmidecode.egg-info

.PHONY: all build install package source_pkg bin_pkg