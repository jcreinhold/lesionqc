#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup

Module installs lesionqc package
Can be run via command: python setup.py install (or develop)

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Feb 11, 2020
"""

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

args = dict(
    name='lesionqc',
    version='0.1.1',
    description="Quality control/metrics for lesion segmentation",
    long_description=readme,
    author='Jacob Reinhold',
    author_email='jacob.reinhold@jhu.edu',
    url='https://github.com/jcreinhold/lesionqc',
    license=license,
    packages=find_packages(exclude=('tests', 'tutorials', 'docs')),
    entry_points = {
        'console_scripts': ['lesion-quality=lesionqc.exec.lesion_quality:main']
    },
    keywords="medical image lesion segmentation quality",
)

setup(install_requires=['numpy',
                        'pandas',
                        'scikit-image',
                        'scipy'], **args)
