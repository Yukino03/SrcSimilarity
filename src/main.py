#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from mylib import src
from mylib import diff

parser = argparse.ArgumentParser()
parser.add_argument("path1")
parser.add_argument("path2")
args = parser.parse_args()

src1 = src.SrcList(args.path1)
src2 = src.SrcList(args.path2)
diff.cmp_src(src1, src2)
