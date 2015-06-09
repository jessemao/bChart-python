# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = (
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
)

kw = {
    'name': 'bchart',
    'version': '0.1.1',
    'description': 'A Python script for bChart',
    'long_description': open('README.rst', 'rt').read(),
    'author': 'Jingxian Mao',
    'author_email': 'jessemao@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/jessemao/bChart-python',
    'keywords': 'data visualization, bChart, d3',
    'classifiers': classifiers,
    'packages': ['bchart'],
    'package_data': {'bchart': ['*.html']},
    'zip_safe': True,
}

setup(**kw)
