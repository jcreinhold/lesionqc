#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.test_exec

test the lesionqc command line interfaces for runtime errors

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Feb 11, 2020
"""

import os
import shutil
import tempfile
import unittest

from lesionqc.exec.lesion_quality import main as lesion_quality


class TestCLI(unittest.TestCase):

    def setUp(self):
        wd = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(wd, 'test_data', 'images')
        self.mask_dir = os.path.join(wd, 'test_data', 'masks')
        self.out_dir = tempfile.mkdtemp()
        self.train_args = f'-s {self.data_dir} -t {self.data_dir}'.split()
        self.predict_args = f'-s {self.data_dir} -o {self.out_dir}/test'.split()

    def test_lesion_quality_cli(self):
        args = f'-s {self.data_dir} -t {self.data_dir} -o {self.out_dir}'.split()
        retval = lesion_quality(args)
        self.assertEqual(retval, 0)

    def tearDown(self):
        shutil.rmtree(self.out_dir)


if __name__ == '__main__':
    unittest.main()
