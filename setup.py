#!/usr/bin/env python
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
  name = 'anyconf',
  version = '0.1.0',
  description = 'Load configuration data from many file formats',
  url = 'https://github.com/tctimmeh/anyconf',
  author = 'Tim Court',
  author_email = 'tctimmeh@gmail.com',
  maintainer = 'Tim Court',
  maintainer_email = 'tctimmeh@gmail.com',

  package_dir = {'': 'src'},
  packages = find_packages('src'),

  install_requires = [
  ],

  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'License :: Freely Distributable',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
)
