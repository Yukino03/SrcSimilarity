#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mylib import src
from mylib import diff

src1 = src.SrcList(__file__)
for x in src1:
  print(x)
x = src1.tokenize_a()