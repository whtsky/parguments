# Copyright (c) 2010 by Dan Jacob.
#
# Some rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided
# with the distribution.
#
# * The names of the contributors may not be used to endorse or
# promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import getpass


try:
    assert raw_input
    assert basestring
except NameError:
    raw_input = input
    basestring = str


def prompt(name, default=None):
    """
    Grab user input from command line.

    :param name: prompt text
    :param default: default value if no input provided.
    """

    prompt = name + (default and ' [%s]' % default or '')
    prompt += name.endswith('?') and ' ' or ': '
    while True:
        rv = raw_input(prompt)
        if rv:
            return rv
        if default is not None:
            return default


def prompt_pass(name, default=None):
    """
    Grabs hidden (password) input from command line.

    :param name: prompt text
    :param default: default value if no input provided.
    """

    prompt = name + (default and ' [%s]' % default or '')
    prompt += name.endswith('?') and ' ' or ': '
    while True:
        rv = getpass.getpass(prompt)
        if rv:
            return rv
        if default is not None:
            return default


def prompt_bool(name, default=False, yes_choices=None, no_choices=None):
    """
    Grabs user input from command line and converts to boolean
    value.

    :param name: prompt text
    :param default: default value if no input provided.
    :param yes_choices: default 'y', 'yes', '1', 'on', 'true', 't'
    :param no_choices: default 'n', 'no', '0', 'off', 'false', 'f'
    """

    yes_choices = yes_choices or ('y', 'yes', '1', 'on', 'true', 't')
    no_choices = no_choices or ('n', 'no', '0', 'off', 'false', 'f')

    while True:
        rv = prompt(name + '?', default and yes_choices[0] or no_choices[0])
        if not rv:
            return default
        if rv.lower() in yes_choices:
            return True
        elif rv.lower() in no_choices:
            return False


def prompt_choices(name, choices, default=None, no_choice=('none',)):
    """
    Grabs user input from command line from set of provided choices.

    :param name: prompt text
    :param choices: list or tuple of available choices. Choices may be
                    single strings or (key, value) tuples.
    :param default: default value if no input provided.
    :param no_choice: acceptable list of strings for "null choice"
    """

    _choices = []
    options = []

    for choice in choices:
        if isinstance(choice, basestring):
            options.append(choice)
        else:
            options.append("%s [%s]" % (choice[1], choice[0]))
            choice = choice[0]
        _choices.append(choice)

    while True:
        rv = prompt(name + '? - (%s)' % ', '.join(options), default)
        rv = rv.lower()
        if rv in no_choice:
            return None
        if rv in _choices:
            return rv
