# encoding = utf-8
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import unittest
import io
import codecs
import os
import sys

import vxTrader

here = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

readme = 'README.md'
if os.path.exists('README.rst'):
    readme = 'README.rst'

with open(readme, 'rb') as f:
    long_description = f.read().decode('utf-8')


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='vxTrader',
    version=vxTrader.__version__,
    url='https://github.com/vex1023/vxTrader/',
    license='The MIT License (MIT)',
    author='vex1023',
    tests_require=['pytest'],
    install_requires=requirements,
    cmdclass={'test': PyTest},
    author_email='vex1023@qq.com',
    description='vxTrader: A Chinese WebAPI wrapper',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    test_suite='vxTrader.tests.test_vxTrader',
    classifiers=[
        'Programming Language :: Python3.5',
        'Development Status :: 4 - Beta',
        'Natural Language :: Chinese',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The MIT License (MIT)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
