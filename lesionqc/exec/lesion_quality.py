#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lesionqc.exec.lesion_quality

command line interface to calculate a suite of metrics for
evaluating lesion segmentation results for NIfTI images

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Mar. 10, 2020
"""

import argparse
from glob import glob
import logging
import os
import sys
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=FutureWarning)
    warnings.filterwarnings('ignore', category=UserWarning)
    import nibabel as nib
    import pandas as pd
    from lesionqc import *


def arg_parser():
    parser = argparse.ArgumentParser(description='Calculate a suite of lesion quality metrics '
                                                 'for a set of NIfTI binary (lesion) segmentations.')

    required = parser.add_argument_group('Required')
    required.add_argument('-p', '--pred-dir', type=str, required=True,
                        help='path to directory of predictions images')
    required.add_argument('-t', '--truth-dir', type=str, required=True,
                          help='path to directory of corresponding truth images')
    required.add_argument('-o', '--out-file', type=str, required=True,
                          help='path to output csv file of results')

    options = parser.add_argument_group('Optional')
    options.add_argument('-v', '--verbosity', action="count", default=0,
                         help="increase output verbosity (e.g., -vv is more than -v)")
    return parser


def glob_imgs(path, ext='*.nii*'):
    """ grab all `ext` files in a directory and sort them for consistency """
    fns = sorted(glob(os.path.join(path, ext)))
    return fns


def split_filename(filepath):
    """ split a filepath into the directory, base, and extension """
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext


def main(args=None):
    args = arg_parser().parse_args(args)
    if args.verbosity == 1:
        level = logging.getLevelName('INFO')
    elif args.verbosity >= 2:
        level = logging.getLevelName('DEBUG')
    else:
        level = logging.getLevelName('WARNING')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
    logger = logging.getLogger(__name__)
    try:
        pred_fns = glob_imgs(args.pred_dir)
        truth_fns = glob_imgs(args.truth_dir)
        if len(pred_fns) != len(truth_fns) or len(pred_fns) == 0:
            raise ValueError(f'Number of predicition and truth images must be equal and non-zero '
                             f'(# Pred.={len(pred_fns)}; # Truth={len(truth_fns)})')
        dcs, jis, ppvs, tprs, lfprs, ltprs, avds = [], [], [], [], [], [], []
        pfns, tfns = [], []
        for pf, tf in zip(pred_fns, truth_fns):
            _, pfn, _ = split_filename(pf)
            _, tfn, _ = split_filename(tf)
            pfns.append(pfn)
            tfns.append(tfn)
            pred, truth = (nib.load(pf).get_fdata() > 0), (nib.load(tf).get_fdata() > 0)
            dcs.append(dice(pred, truth))
            jis.append(jaccard(pred, truth))
            ppvs.append(ppv(pred, truth))
            tprs.append(tpr(pred, truth))
            lfprs.append(lfpr(pred, truth))
            ltprs.append(ltpr(pred, truth))
            avds.append(avd(pred, truth))
            logger.info(f'Pred: {pfn}; Truth: {tfn}; Dice: {dcs[-1]:0.2f}; Jacc: {jis[-1]:0.2f}; PPV: {ppvs[-1]:0.2f}; '
                        f'TPR: {tprs[-1]:0.2f}; LFPR: {lfprs[-1]:0.2f}; LTPR: {ltprs[-1]:0.2f}; AVD: {avds[-1]:0.2f}')
        out = {'Pred': pfns,
               'Truth': tfns,
               'Dice': dcs,
               'Jaccard': jis,
               'PPV': ppvs,
               'TPR': tprs,
               'LFPR': lfprs,
               'LTPR': ltprs,
               'AVD': avds}
        pd.DataFrame(out).to_csv(args.out_file)
        return 0
    except Exception as e:
        logger.exception(e)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
