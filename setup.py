#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011-2013 by Łukasz Langa
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import codecs
from setuptools import setup, find_packages

PY3 = sys.version_info[0] == 3

if not PY3:
    reload(sys)
    sys.setdefaultencoding('utf8')

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', 'utf8',
) as ld_file:
    long_description = ld_file.read()
# We let it die a horrible tracebacking death if reading the file fails.
# We couldn't sensibly recover anyway: we need the long description.

setup (
    name = 'null',
    version = '0.6.0',
    author = 'Łukasz Langa',
    author_email = 'lukasz@langa.pl',
    description = "Implements the null object pattern.",
    long_description = long_description,
    url = 'https://bitbucket.org/ambv/null',
    keywords = '',
    platforms = ['any'],
    license = 'MIT',
    py_modules = ['null'],
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False, # if only because of the readme file
    install_requires = [
        'six',
    ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
