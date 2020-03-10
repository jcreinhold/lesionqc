#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
metrics

holds metric function definitions

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Mar. 10, 2020
"""

__all__ = ['dice',
           'jaccard',
           'ppv',
           'tpr',
           'lfpr',
           'ltpr',
           'avd',
           'assd']

import numpy as np
from skimage.measure import label


def dice(pred, truth):
    """ dice coefficient between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    intersection = (p & t).sum()
    cardinality = p.sum() + t.sum()
    if cardinality == 0.: return None
    return 2 * intersection / cardinality


def jaccard(pred, truth):
    """ jaccard index (IoU) between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    intersection = (p & t).sum()
    union = (p | t).sum()
    if union == 0.: return None
    return intersection / union


def ppv(pred, truth):
    """ positive predictive value (precision) between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    intersection = (p & t).sum()
    denom = p.sum()
    if denom == 0.: return None
    return intersection / denom


def tpr(pred, truth):
    """ true positive rate (sensitivity) between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    intersection = (p & t).sum()
    denom = t.sum()
    if denom == 0.: return None
    return intersection / denom


def lfpr(pred, truth):
    """ lesion false positive rate between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    cc, n = label(p, return_num=True)
    count = 0
    for i in range(1, n+1):
        if ((cc == i) & t).sum() == 0:
            count += 1
    return count / n


def ltpr(pred, truth):
    """ lesion true positive rate between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    cc, n = label(t, return_num=True)
    count = 0
    for i in range(1, n+1):
        if ((cc == i) & p).sum() > 0:
            count += 1
    return count / n


def avd(pred, truth):
    """ absolute volume difference between predicted and true binary pred """
    p, t = (pred > 0), (truth > 0)
    numer = np.abs(p.sum() - t.sum())
    denom = t.sum()
    if denom == 0.: return None
    return numer / denom


def assd(pred, truth):
    """ average symmetric surface difference between predicted and true binary pred """
    raise NotImplementedError
