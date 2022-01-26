# coding: utf-8

import os
import sys

from setuptools import setup
from codecs import open

NAME = "xumm-sdk-py-dangell7"
VERSION = "v0.9.9-beta.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# Get the long description from the README.md file
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description='Xumm SDK for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='xrpl-labs',
    author_email='support@xrpl-labs.com',
    url='https://github.com/CASL-AE/xumm-sdk-py',
    packages=[
        'xumm',
        'xumm.resource',
        'xumm.resource.types',
        'xumm.resource.types.xumm_api',
        'xumm.resource.types.meta',
        'xumm.resource.types.payload',
        'xumm.resource.types.storage'
    ],
    test_suite='pytest',
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
