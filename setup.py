# coding: utf-8
import os
from setuptools import setup, find_packages
from codecs import open

NAME = "xumm-sdk-py"
VERSION = "1.0.2"

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
    author='XRPL-Labs',
    author_email='support@xrpl-labs.com',
    url='https://github.com/XRPL-Labs/xumm-sdk-py',
    packages=find_packages(include=('xumm*',)),
    include_package_data=True,
    install_requires=[
        "requests>=2.26.0",
        "websocket-client==1.2.3",
        "six==1.16.0",
        "python-dotenv==0.19.2"
    ],
    extras_require={
        'develop': [
            'pytest==6.2.5',
            'websockets==9.1',
            'flake8==4.0.1'
        ]
    },
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
    keywords='xrp, ledger, ripple, xumm, sdk'
)
