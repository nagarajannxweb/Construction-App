# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in construction_app/__init__.py
from construction_app import __version__ as version

setup(
	name='construction_app',
	version=version,
	description='nxweb construction app',
	author='nxweb',
	author_email='info@nxweb.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
