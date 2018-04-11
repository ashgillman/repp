#!/usr/bin/env python3

import os
from setuptools import setup, find_packages


setup(
    name='repp',
    description='Manage repositories.',
    author='Ashely Gillman',
    version='1.0.0',
    license='MIT',
    py_modules=['repp'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        repp=repp:cli
    ''',
)
