# coding: utf-8

import os
import sys

from setuptools import setup
from codecs import open

NAME = "xumm-sdk-python"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# Get the long description from the README.md file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Don't import xumm module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xumm'))

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    description='Xumm SDK for Python',
    long_description=long_description,
    license='MIT',
    author='xrpl-labs',
    author_email='support@xrpl-labs.com',
    url='https://github.com/CASL-AE/xumm-sdk-py',
    packages=['xumm', 'xumm.resource'],
    # install_requires=['requests >= 2.27.1', 'websocket-client >= 1.2.3','six >= 1.16.0'],  # noqa: E501
    install_requires=required,
    test_suite='pytest',
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 01 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
