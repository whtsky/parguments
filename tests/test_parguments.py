"""
Usage:
    parguments add <name>
    parguments remove <name>
"""

from parguments import Parguments
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
    p.run(command="add", argv=["remove", "catsup"], exit=False)

    import sys
    sys.argv[1:] = ["add", "catsup"]

    p.run(exit=False)

    try:
        p.run(argv=["remove", "wordpress"])
    except SystemExit:
        pass
    else:
        raise
