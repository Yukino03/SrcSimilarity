#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mylib import src
from mylib import diff

src1 = src.SrcList(__file__)
# for x in range(len(src1)):
  # print(src1.tokenize(x))

# wordを数える
dic = {}
for x in range(len(src1)):
  line = src1.tokenize(x)
  for token in line:
    if token in dic:
      dic[token] = dic[token]+1
    else :
      dic[token] = 1
dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse = True)
for word in dic_sorted:
  print(word)
