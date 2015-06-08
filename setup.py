# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = (
    'Development Status :: 0.1.0',
    'Programming Language :: Python :: 2.7',
    'License :: MIT License',
)

kw = {
    'name': 'bChart',
    'version': '0.1.0',
    'description': 'A Python script for bChart',
    'long_description': open('README.rst', 'rt').read(),
    'author': 'Jingxian Mao',
    'author_email': 'jessemao@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/wrobstory/vincent',
    'keywords': 'data visualization',
    'classifiers': classifiers,
    'packages': ['vincent'],
    'package_data': {'vincent': ['*.html']},
    'install_requires': required,
    'zip_safe': True,
}

setup(**kw)
