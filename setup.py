#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
 

setup(
    name="oudjirasign",
    version="0.0.1",
    description="oudjirasign est un module python de signature electronique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/oumar90/oudjirasign",
    author="Oumar Djimé Ratou",
    author_email="oudjira90@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["oudjirasign"],
    include_package_data=True,
    install_requires=["pycrypto"],
    entry_points={
        "console_scripts": [
            "oudjirasign=oudjirasign.oudjirasign:main",
        ]
    },
)