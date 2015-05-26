#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'tencentyun',
    version = '1.0.1',
    keywords = ('tencentyun', 'qcloud'),
    description = 'python sdk for app.qcloud.com',
    license = 'MIT License',
    install_requires = [],

    author = 'jayli',
    author_email = 'jayli@tencent.com',
    
    packages = find_packages(),
    platforms = 'any',
)