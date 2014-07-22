# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import scanner_frontend
version = scanner_frontend.__version__

setup(
    name='scanner_frontend',
    version=version,
    author='',
    author_email='vincentnys@gmail.com',
    packages=[
        'scanner_frontend',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['scanner_frontend/manage.py'],
)