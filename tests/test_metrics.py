#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.test_metrics

test the functions located in metrics submodule for runtime errors

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Mar. 10, 2020
"""

import os
import unittest

import nibabel as nib

from lesionqc.metrics import *


class TestUtilities(unittest.TestCase):

    def setUp(self):
        wd = os.path.dirname(os.path.abspath(__file__))
        pred_fn = os.path.join(wd, 'test_data', 'pred', 'pred.nii.gz')
        truth_fn = os.path.join(wd, 'test_data', 'truth', 'truth.nii.gz')
        self.pred = nib.load(pred_fn).get_fdata()
        self.truth = nib.load(truth_fn).get_fdata()

    def test_dice(self):
        dice_coef = dice(self.pred, self.truth)
        correct = 2 * (3 / ((8 + 1 + 1) + (2 + 1 + 1)))
        self.assertEqual(dice_coef, correct)

    def test_jaccard(self):
        jaccard_idx = jaccard(self.pred, self.truth)
        correct = (3 / ((8 + 1 + 1) + 1))
        self.assertEqual(jaccard_idx, correct)

    def test_ppv(self):
        ppv_score = ppv(self.pred, self.truth)
        correct = (3 / (2 + 1 + 1))
        self.assertEqual(ppv_score, correct)

    def test_tpr(self):
        tpr_score = tpr(self.pred, self.truth)
        correct = (3 / (8 + 1 + 1))
        self.assertEqual(tpr_score, correct)

    def test_lfpr(self):
        lfpr_score = lfpr(self.pred, self.truth)
        correct = 1 / 3
        self.assertEqual(lfpr_score, correct)

    def test_ltpr(self):
        ltpr_score = ltpr(self.pred, self.truth)
        correct = 2 / 3
        self.assertEqual(ltpr_score, correct)

    def test_avd(self):
        avd_score = avd(self.pred, self.truth)
        correct = 0.6
        self.assertEqual(avd_score, correct)

    def test_corr(self):
        ps = self.pred.sum()
        ts = self.truth.sum()
        eps = 0.1
        pred_vols = [ps, ps+eps, ps-eps]
        truth_vols = [ts, ts+eps, ts-eps]
        corr_score = corr(pred_vols, truth_vols)
        correct = 1.0
        self.assertAlmostEqual(corr_score, correct)

    def test_isbi15_score(self):
        isbi15 = isbi15_score(self.pred, self.truth)
        correct = 0.6408730158730158
        self.assertEqual(isbi15, correct)

    @unittest.skip('Not implemented.')
    def test_assd(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
