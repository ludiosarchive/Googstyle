#!/usr/bin/env python

from distutils.core import setup

import googstyle

setup(
	name='googstyle',
	version=googstyle.__version__,
	packages=['googstyle'],
	package_data={'googstyle': ['goog-images/*']},
)
