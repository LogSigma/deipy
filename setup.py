# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 01:40:10 2019

@author: Sky
"""

from setuptools import setup, find_packages

setup(
    name             = 'deipy',
    version          = '1.0',
    description      = 'Data Analysis Engine',
    long_description = open('README.md').read(),
    author           = 'Jisu Lee',
    author_email     = 'logsigma@naver.com',
    url              = 'https://github.com/logisgma/deipy',
    download_url     = 'https://github.com/logisgma/deipy',
    install_requires = ['requests'],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['bot', 'study', 'api'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
    ]
)