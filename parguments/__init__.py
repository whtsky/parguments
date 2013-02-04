# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = 'whtsky'
__version__ = '0.2'

import sys
import inspect
from docopt import docopt
from .cli import *


class Command(object):
    """
    Base class for creating commands.
    """
    def __init__(self, func, doc=None):
        self._func = func
        description = doc or func.__doc__
        self.doc = description.strip()

    def __call__(self, *args, **kwargs):
        self._func(*args, **kwargs)


class Parguments(object):
    def __init__(self, doc, argv=None, help=True, version=None,
                 options_first=False):
        """
        Init a new parguments instance.
        Note that parguments uses [docopt](https://github.com/docopt/docopt)
        to parse arguments.

        :param doc: description of your program.

        """
        self.doc = doc
        self._argv = argv
        self._help = help
        self._version = version
        self._options_first = options_first
        self._commands = {}

    def command(self, func):
        """
        Decorator to add a command function to the registry.

        :param func: command function.

        """
        command = Command(func)
        self._commands[func.__name__] = command

    def add_command(self, func, name=None, doc=None):
        """
        Add a command function to the registry.

        :param func: command function.
        :param name: default name of func.
        :param doc: description of the func.default docstring of func.

        """
        command = Command(func, doc)
        name = name or func.__name__
        self._commands[name] = command

    def parse(self, doc, help=None):
        if help is None:
            help = self._help
        args = docopt(doc, self._argv, help, self._version,
            self._options_first)
        return args

    def run(self, command=None, default_command=None, fallback=None):
        """
        Parse arguments and run the funcs.

        :param command: name of command to run. default sys.argv[1]
        :param default_command: name of default command to run
            if no arguments passed.
        :param fallback: if no command is found, we'll call this func.
        """
        args = self.parse(self.doc, help=False)
        result = 0
        cmd = args.get(command, default_command)
        if command is None and len(sys.argv) > 1:
            cmd = sys.argv[1]

        if cmd in self._commands:
            cmd = self._commands[cmd]
            if not inspect.getargspec(cmd._func).args:
                # Seemed that command doesn't want any argument.
                result = cmd()
            else:
                result = cmd(args=args)
        elif fallback:
            fallback(cmd, args)
        else:
            self.parse(self.doc)
        sys.exit(result or 0)
