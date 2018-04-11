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
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    keywords = 'git repository manager',
)
