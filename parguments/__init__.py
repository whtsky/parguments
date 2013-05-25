# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys
from docopt import docopt
from .cli import *
from .utils import remove_indentation


class Command(object):
    """
    Base class for creating commands.
    """
    def __init__(self, func, doc=None):
        self._func = func
        description = doc or func.__doc__
        self.doc = remove_indentation(description)

    def __call__(self, **kwargs):
        self._func(**kwargs)


class Parguments(object):
    '''
    Parguments is a python library to help you create human
    friendly cli written on top of docopt.

    Example ::

        """
        catsup v1.0

        Usage:
            catsup init [<path>]
            catsup build
            catsup deploy
            catsup -h | --help
            catsup --version

        Options:
            -h --help             Show this screen and exit.
            -s --settings=<file>  path to config file. [default: config.json]
        """
        from parguments import Parguments

        parguments = Parguments(__doc__, version='1.0')

        @parguments.command
        def init(path):
          """
          Usage:
            catsup init [<path>]

          Options:
            -h --help             Show this screen and exit.
            -s --settings=<file>  path to setting file. [default: config.json]
          """
          pass

        @parguments.command
        def build(settings):
          """
          Usage:
            catsup build [-s <file>|--settings=<file>]

          Options:
            -h --help             Show this screen and exit.
            -s --settings=<file>  path to setting file. [default: config.json]
          """
          pass

        @parguments.command
        def deploy(settings):
          """
          Usage:
            catsup deploy [-s <file>|--settings=<file>]

          Options:
            -h --help             Show this screen and exit.
            -s --settings=<file>  path to setting file. [default: config.json]
          """
          pass

        if __name__ == '__main__':
          parguments.run()



    :param doc: description of your program.
    :type doc: str

    :param version: the object will be printed if
     ``--version`` is in ``argv``
    :type version: any object

    :param options_first: Set to True to require
     options precede positional arguments,

     i.e. to forbid options and positional arguments intermix.
    :type options_first: bool

    '''

    def __init__(self, doc, version=None, options_first=False):
        self.doc = doc
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

    def parse(self, doc, argv, help, first=False):
        if first and argv not in [['-h'], ['--help']]:
            argv = [x for x in argv if x not in ['-h', '--help']]
        args = docopt(doc, argv, help, self._version,
                      self._options_first)
        return args

    def process_args(self, args):
        kwargs = {}
        for k, v in args.items():
            if k not in self._commands:
                k = k.lstrip('-')
                k = k.strip('<>')
                kwargs[k] = v
        return kwargs

    def run(self, command=None, argv=None, help=True, exit=True):
        """
        Parse arguments and run the funcs.

        :param command: name of command to run. default argv[0]
        :param argv: argument vector to be parsed.
            sys.argv[1:] is used if not provided.
        :param help: Set to False to disable automatic
            help on -h or --help options.
        :param exit: Set to False to return result instead of exiting.
        """

        result = 0
        if argv is None:
            argv = sys.argv[1:]

        args = self.parse(self.doc, argv=argv, help=help, first=True)

        if command is None and len(sys.argv) > 1:
            cmd = argv[0]
        else:
            cmd = args.get(command, None)

        if cmd in self._commands:
            cmd = self._commands[cmd]
            args = self.parse(cmd.doc, argv=argv, help=help)
            args = self.process_args(args)
            result = cmd(**args)

        if exit:
            sys.exit(result)
        return result
