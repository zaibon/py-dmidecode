"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="py-dmidecode",
    version="0.1.0",
    description="python lib that parse the output of dmidecode ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaibon/py-dmidecode",
    author="Christophe de Carvalho",
    # author_email='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="system development",
    py_modules=["dmidecode"],
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={
        "Bug Reports": "https://github.com/zaibon/py-dmidecode/issues",
        "Source": "https://github.com/zaibon/py-dmidecode/",
    },
)
