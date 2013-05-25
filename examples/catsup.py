#!/usr/bin/env python
"""
catsup v1.0

Usage:
    catsup init [<path>]
    catsup build
    catsup deploy
    catsup -h | --help
    catsup --version

Options:
    -h --help               show this screen.
    -s --settings=<file>    specify a config file. [default: config.json]
"""
from parguments import Parguments

parguments = Parguments(__doc__, version='1.0')

@parguments.command
def init(path):
    """
    Usage:
        catsup init [<path>]

    Options:
        -h --help               show this screen.
        -s --settings=<file>    specify a setting file. [default: config.json]
    """
    pass

@parguments.command
def build(settings):
    """
    Usage:
        catsup build [-s <file>|--settings=<file>]

    Options:
        -h --help               show this screen.
        -s --settings=<file>    specify a setting file. [default: config.json]
    """
    pass

@parguments.command
def deploy(settings):
    """
    Usage:
        catsup deploy [-s <file>|--settings=<file>]

    Options:
        -h --help               show this screen.
        -s --settings=<file>    specify a setting file. [default: config.json]
    """
    pass

if __name__ == '__main__':
    parguments.run()
