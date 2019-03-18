#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tokenize import tokenize,untokenize

class SrcList():
  def __init__(self, path):
    self.path = path
    self.read_file(path)
    self._i = 0
    self.tokenize()

  def __len__(self):
    return len(self.lines)

  def __getitem__(self, index):
    return self.lines[index]

  def read_file(self, filepath):
    with open(filepath) as f:
      self.lines = [s.rstrip() for s in f.readlines()]
      self.it = iter(self.lines)

  def print_src(self):
    for line in self.lines:
      print(line)

  def get_lineb(self, n):
    return self.lines[n].encode(encoding="utf-8")

  def tokenize_a(self, byterow):
    '''tokenize a line.FIXME'''
    tmp = tokenize(byterow.readline)
    return tmp

  def tokenize(self):
    '''FIXME'''
    print("stab")

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
