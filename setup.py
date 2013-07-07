"""

parguments
==========

A simple cli args parser for Python.

Useful for creating command-line scripts.

Example ::

    \"""
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
    \"""
    from parguments import Parguments

    parguments = Parguments(__doc__, version='1.0')

    @parguments.command
    def init(path):
      \"""
      Usage:
        catsup init [<path>]

      Options:
        -h --help             Show this screen and exit.
        -s --settings=<file>  path to setting file. [default: config.json]
      \"""
      pass

    @parguments.command
    def build(settings):
      \"""
      Usage:
        catsup build [-s <file>|--settings=<file>]

      Options:
        -h --help             Show this screen and exit.
        -s --settings=<file>  path to setting file. [default: config.json]
      \"""
      pass

    @parguments.command
    def deploy(settings):
      \"""
      Usage:
        catsup deploy [-s <file>|--settings=<file>]

      Options:
        -h --help             Show this screen and exit.
        -s --settings=<file>  path to setting file. [default: config.json]
      \"""
      pass

    if __name__ == '__main__':
      parguments.run()

Documents at http://parguments.rtfd.org/
"""

from setuptools import setup, find_packages

setup(
    name='parguments',
    version='0.3.2',
    author='whtsky',
    author_email='whtsky@me.com',
    url='https://github.com/whtsky/parguments',
    packages=find_packages(),
    description='Parguments: A simple cli args parser for Python',
    long_description=__doc__,
    include_package_data=True,
    install_requires=['docopt>=0.6.1'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
)
