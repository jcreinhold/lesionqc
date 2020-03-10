#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.test_exec

test the lesionqc command line interfaces for runtime errors

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Mar. 10, 2020
"""

import os
import shutil
import tempfile
import unittest

from lesionqc.exec.lesion_quality import main as lesion_quality


class TestCLI(unittest.TestCase):

    def setUp(self):
        wd = os.path.dirname(os.path.abspath(__file__))
        self.pred_dir = os.path.join(wd, 'test_data', 'pred')
        self.truth_dir = os.path.join(wd, 'test_data', 'truth')
        self.out_dir = tempfile.mkdtemp()
        self.out_file = os.path.join(self.out_dir, 'test.csv')
        self.args = f'-p {self.pred_dir} -t {self.truth_dir} -o {self.out_file}'.split()

    def test_lesion_quality_cli(self):
        retval = lesion_quality(self.args)
        self.assertEqual(retval, 0)

    def tearDown(self):
        shutil.rmtree(self.out_dir)


if __name__ == '__main__':
    unittest.main()
