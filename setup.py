#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup, find_packages

import parguments

setup(
    name='parguments',
    version=parguments.__version__,
    author=parguments.__author__,
    author_email='whtsky@me.com',
    url='https://github.com/whtsky/parguments',
    packages=find_packages(),
    description='Parguments: A simple cli args parser for Python',
    long_description=open('README.rst').read(),
    install_requires=[
        'docopt'
    ],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    **kwargs
)
