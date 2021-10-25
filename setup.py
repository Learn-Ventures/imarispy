#!/usr/bin/env python

import setuptools


install_requires = []

setuptools.setup(
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)
