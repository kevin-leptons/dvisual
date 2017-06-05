#!/usr/bin/env python

'''
SYNOPSIS

    pip install -e .

DESCRIPTION

    Metadata for this package.

REFERENCES

    Building and Distributing Packages with Setuptools
        http://setuptools.readthedocs.io/en/latest/setuptools.html
'''

from setuptools import setup, find_packages


setup(
    name='dvisual',
    version='0.1.0',
    description='Fast way to make data visualization',
    keywords='data visualization python3',
    author='Kevin Leptons',
    author_email='kevin.leptons@gmail.com',
    url='https://github.com/kevin-leptons/dvisual',
    download_url='https://github.com/kevin-leptons/dvisual',
    install_requires=[
        'pygal==2.3.1', 'lxml==3.8.0'
    ],
    packages=find_packages(exclude=['tool', 'test']),
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
