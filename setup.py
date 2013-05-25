import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup, find_packages

setup(
    name='parguments',
    version='0.3.0',
    author='whtsky',
    author_email='whtsky@me.com',
    url='https://github.com/whtsky/parguments',
    packages=find_packages(),
    description='Parguments: A simple cli args parser for Python',
    long_description=open('README.md').read(),
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
    **kwargs
)
