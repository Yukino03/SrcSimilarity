#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tokenize import tokenize,untokenize
from io import BytesIO
class SrcList():
  def __init__(self, path):
    self.path = path
    self.read_file(path)
    self._i = 0

  def __len__(self):
    return len(self.lines)

  def __getitem__(self, index):
    return self.lines[index]

  def read_file(self, filepath):
    with open(filepath) as f:
      self.lines = [s.rstrip() for s in f.readlines()]
      self.it = iter(self.lines)
    with open(filepath) as d:
      self.tokens = [s.encode() for s in d.readlines()]

  def print_src(self):
    for line in self.lines:
      print(line)

  def get_lineb(self, n):
    return self.lines[n].encode(encoding="utf-8")

  def tokenize_a(self, n):
    '''raw tokenize a line(By line num)'''
    result = []
    tmp = tokenize(BytesIO(self.get_lineb(n)).readline)
    for toknum, tokval, _, _, _ in tmp:
      result.append((toknum, tokval))
    return result

  def tokenize(self,n):
    '''practical tokenize'''
    result = []
    tmp = tokenize(BytesIO(self.get_lineb(n)).readline)
    for _, tokval, _, _, _ in tmp:
      if tokval != '':
        result.append(tokval)
    if len(result) > 0:
      result.pop(0)
    return result

  def get_path(self):
    return self.path

  def __iter__(self):
    return self

  def __next__(self):
    if self._i < len(self):
        value = self[self._i]
        self._i += 1
        return value
    else :
      self._i = 0
      raise StopIteration()

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("Argument Error")
    sys.exit(1)
  else:
    src = SrcList(args[1])
    src.print_src()
    print(src.get_line(0))
    sys.exit(0)
