#!/usr/bin/python3

from setuptools import setup
import stepan

setup(
	name = 'stepan',
	version = stepan.__version__,
	packages = ['stepan'],
	author = 'mirmik',
	author_email = 'mirmikns@yandex.ru',
	description = 'Stepan Library',
	long_description=open("README.md", "r").read(),
	long_description_content_type='text/markdown',
	license='MIT',
	url = 'https://github.com/mirmik/stepan',
	scripts = ["scripts/mirmik-was-here"],
)