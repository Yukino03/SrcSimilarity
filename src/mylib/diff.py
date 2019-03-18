#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from tokenize import tokenize
from io import BytesIO
# compare srcs
def cmp_src(src1, src2):
  print("stab")

# compare lines
def cmp_line(line1, line2):
  return line1 == line2

# func() -> func
def extract_func(line):
# .*(?=\(.*\))
# 対応した括弧より前を抽出
  result = re.compile(".*(?=\(.*\))").match(line)
# 後方から見て最初の空白orカンマまでを抽出
# result = re.compile("").match(line)
  return result