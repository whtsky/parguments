# -*- coding: utf-8 -*-

__author__ = 'whtsky'
__version__ = '0.1'

import sys
from docopt import docopt


class Command(object):
    """
    Base class for creating commands.
    """
    def __init__(self, func, doc=''):
        self._func = func
        description = doc or func.__doc__
        self.doc = description.strip()

    def __call__(self, *args, **kwargs):
        self._func(*args, **kwargs)


class Parguments(object):
    def __init__(self, doc, *args, **kwargs):
        """
        Init a new parguments instance.
        Note that parguments uses [docopt](https://github.com/docopt/docopt)
        to parse arguments.

        :param doc: description of your program.

        """
        self.doc = doc
        self._args = args
        self._kwargs = kwargs
        self._commands = {}

    def command(self, func):
        """
        Decorator to add a command function to the registry.

        :param func: command function.

        """
        command = Command(func)
        self._commands[func.__name__] = command

    def add_command(self, func, name='', doc=''):
        """
        Add a command function to the registry.

        :param func: command function.
        :param name: name of command.func.__name__ by default.
        :param doc: description of the func.func.__doc__ by default.

        """
        command = Command(func, doc)
        name = name or func.__name__
        self._commands[name] = command

    def run(self, default_command=''):
        command = default_command
        if len(sys.argv) > 1:
            command = sys.argv[1]

        if command in self._commands:
            args = docopt(self._commands[command].doc,
                *self._args, **self._kwargs)
            result = self._commands[command](args=args)
        else:
            docopt(self.doc, *self._args, **self._kwargs)
            result = 0
        sys.exit(result or 0)
