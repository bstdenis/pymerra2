from __future__ import print_function

import os
from codecs import open

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Command line script will not be created.")
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
about = {}

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(here, 'pymerra2', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    # long_description_content_type='text/markdown',
    url=about["__url__"],
    packages=find_packages(),
    classifiers=(
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ),
)