#!/usr/bin/env python

from distutils.core import setup

import googstyle

setup(
	name='googstyle',
	version=googstyle.__version__,
	description="CSS and images extracted from Closure Library",
	url="https://github.com/ludios/Googstyle",
	author="Ivan Kozik",
	author_email="ivan@ludios.org",
	classifiers=[
		'Development Status :: 3 - Beta',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Topic :: Internet :: WWW/HTTP',
		'License :: OSI Approved :: Apache Software License',
	],
	packages=['googstyle'],
	package_data={'googstyle': ['goog-images/*']},
)
