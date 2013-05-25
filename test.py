"""
Usage:
    parguments add <name>
    parguments remove <name>
"""

import sys

from io import StringIO

from parguments import Parguments
from parguments.cli import *
from parguments.utils import *


def test_utils():
    t = """
    Hi
    Good morning
    >_<
        haha
    """
    assert count_indentation(t) == 4
    assert remove_indentation(t) == """
Hi
Good morning
>_<
    haha
"""

    t += "\n "
    assert count_indentation(t) == 4
    t += "\n  h"
    assert count_indentation(t) == 2
    t += "\nb"
    assert count_indentation(t) == 0


def test_adding_commands():
    p = Parguments(__doc__)
    assert p._commands == {}

    @p.command
    def add(name):
        """
        Usage:
            parguments add <name>
        """
        assert name == "catsup"

    assert 'add' in p._commands

    def remove(name):
        """
        Usage:
            parguments remove <name>
        """
        assert name == "wordpress"

    p.add_command(remove)
    assert 'remove' in p._commands

    p.run(argv=["add", "catsup"], exit=False)
    import sys
    sys.argv[1:] = ["add", "catsup"]

    p.run(exit=False)

    try:
        p.run(argv=["remove", "wordpress"])
        p.run(command="remove", argv=["remove catsup"])
    except SystemExit:
        pass
    else:
        raise


# Tests for parguments.cli


class Catcher(object):
    """Helper decorator to test raw_input."""

    def __init__(self, handler):
        self.handler = handler
        self.inputs = []

    def __enter__(self):
        self.__stdin = sys.stdin
        self.__stdout = sys.stdout
        sys.stdin = self
        sys.stdout = self

    def __exit__(self, type, value, traceback):
        sys.stdin = self.__stdin
        sys.stdout = self.__stdout

    def write(self, value):
        self.__stdout.write(value)
        result = self.handler(value)
        if result is not None:
            self.inputs.append(result)

    def readline(self):
        return self.inputs.pop()

    def getvalue(self):
        return self.__stdout.getvalue()

    def truncate(self, pos):
        return self.__stdout.truncate(pos)


def run(command_line, manager_run, capture_stderr=False):
    """
        Returns tuple of standard output and exit code
    """
    sys_stderr_orig = sys.stderr

    if capture_stderr:
        sys.stderr = StringIO.StringIO()

    sys.argv = command_line.split()
    try:
        manager_run()
    except SystemExit:
        pass
    finally:
        out = sys.stdout.getvalue()
        # clear the standard output buffer
        sys.stdout.truncate(0)
        assert len(sys.stdout.getvalue()) == 0
        if capture_stderr:
            out += sys.stderr.getvalue()
        sys.stderr = sys_stderr_orig

    return out


def test_prompt():
    parguments = Parguments(__doc__)

    @parguments.command
    def add(name):
        """
        Usage:
            parguments add <name>
        """
        print(prompt(name='hello'))

    @Catcher
    def hello_john(msg):
        if "hello" in msg:
            return 'whtsky'

    with hello_john:
        out = run('parguments add a', parguments.run)
        assert 'hello: whtsky' in out


def test_prompt_with_default_prompt():
    parguments = Parguments(__doc__)

    @parguments.command
    def add(name):
        """
        Usage:
            parguments add <name>
        """
        print(prompt(name='hello', default='whtsky'))

    @Catcher
    def hello(msg):
        if "hello" in msg:
            return '\n'

    with hello:
        out = run('parguments add a', parguments.run)
        assert 'hello [whtsky]: whtsky' in out

    @Catcher
    def hello_juliette(msg):
        if "hello" in msg:
            return 'parguments'

    with hello_juliette:
        out = run('parguments add a', parguments.run)
        assert 'hello [whtsky]: parguments' in out


def test_prompt_bool():
    parguments = Parguments(__doc__)

    @parguments.command
    def add(name):
        """
        Usage:
            parguments add <name>
        """
        print(prompt_bool(name='correct', default=True, yes_choices=['y'],
                          no_choices=['n']) and 'yes' or 'no')

    @Catcher
    def correct_default(msg):
        if "correct" in msg:
            return '\n'

    @Catcher
    def correct_y(msg):
        if "correct" in msg:
            return 'y'

    @Catcher
    def correct_n(msg):
        if "correct" in msg:
            return 'n'

    with correct_default:
        out = run('parguments add a', parguments.run)
        assert 'correct? [y] yes' in out

    with correct_y:
        out = run('parguments add a', parguments.run)
        assert 'correct? [y] yes' in out

    with correct_n:
        out = run('parguments add a', parguments.run)
        assert 'correct? [y] no' in out


def test_prompt_choices():
    parguments = Parguments(__doc__)

    @parguments.command
    def add(name):
        """
        Usage:
            parguments add <name>
        """
        print(prompt_choices(name='add via', choices=['rsync', 'cd']))

    @parguments.command
    def remove(name):
        """
        Usage:
            parguments remove <name>
        """
        print(prompt_choices(name='remove via', choices=['rsync', 'cd'],
                             default='rsync'))

    @Catcher
    def choose_default(msg):
        if "via" in msg:
            return '\n'

    @Catcher
    def choose_cd(msg):
        if "via" in msg:
            return 'cd'

    @Catcher
    def choose_none(msg):
        if "via" in msg:
            return 'none'

    with choose_default:
        out = run('parguments remove a', parguments.run)
        assert 'remove via? - (rsync, cd) [rsync]: rsync' in out

    with choose_cd:
        out = run('parguments remove a', parguments.run)
        assert 'remove via? - (rsync, cd) [rsync]: cd' in out

    with choose_cd:
        out = run('parguments add a', parguments.run)
        assert 'add via? - (rsync, cd): cd' in out

    with choose_none:
        out = run('parguments add a', parguments.run)
        assert 'add via? - (rsync, cd): None' in out