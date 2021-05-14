lesionqc
========

**This repo has been deprecated. See [lesion-metrics](https://github.com/jcreinhold/lesion-metrics) for a maintained version.**


[![Build Status](https://api.travis-ci.com/jcreinhold/lesionqc.svg?branch=master)](https://travis-ci.com/jcreinhold/lesionqc)
[![Coverage Status](https://coveralls.io/repos/github/jcreinhold/lesionqc/badge.svg?branch=master)](https://coveralls.io/github/jcreinhold/lesionqc?branch=master)
[![Documentation Status](https://readthedocs.org/projects/lesionqc/badge/?version=latest)](http://lesionqc.readthedocs.io/en/latest/?badge=latest)
[![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

This package supports a suite of quality analysis metrics and tools for lesion segmentation results

This package was developed by [Jacob Reinhold](https://jcreinhold.github.io) and the other students and researchers of the 
[Image Analysis and Communication Lab (IACL)](http://iacl.ece.jhu.edu/index.php/Main_Page).

Requirements
------------

- nibabel (if you want to use the CLI)
- numpy
- pandas
- scikit-image
- scipy

Installation
------------

    pip install git+git://github.com/jcreinhold/lesionqc.git

Tutorial
--------

[5 minute Overview](https://github.com/jcreinhold/lesionqc/blob/master/tutorials/5min_tutorial.md)

Test Package
------------

Unit tests can be run from the main directory as follows:

    nosetests -v tests
