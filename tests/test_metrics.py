#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.test_metrics

test the functions located in metrics submodule for runtime errors

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Feb 11, 2018
"""

import os
import unittest

from synthqc.metrics import *


class TestUtilities(unittest.TestCase):

    def setUp(self):
        wd = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(wd, 'test_data', 'images')
        self.mask_dir = os.path.join(wd, 'test_data', 'masks')
        self.img_fn = os.path.join(self.data_dir, 'test.nii.gz')
        self.mask_fn = os.path.join(self.mask_dir, 'mask.nii.gz')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
