from __future__ import print_function

import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
about = {}

with codecs.open("README.md", "r") as fh:
    long_description = fh.read()

with codecs.open(os.path.join(here, 'pymerra2', '__init__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

INSTALL_REQUIRES = [line.strip() for line in open('requirements.txt')]

setup(
    # -- meta information --------------------------------------------------
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    url=about["__url__"],
    classifiers=[
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
    ],

    # -- Package structure -------------------------------------------------
    packages=find_packages(),

    include_package_data=True,
    install_requires=INSTALL_REQUIRES,

)
