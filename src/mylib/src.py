#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Src():
  def __init__(self, filepath):
    self.__path = filepath
    self.read_file(filepath)

  def read_file(self, filepath):
    with open(filepath) as f:
      self.__lines = [s.rstrip() for s in f.readlines()]

  def print_src(self):
    for line in self.__lines:
      print(line)

  def get_line(self, n):
    return self.__lines[n]

  def get_path(self):
    return self.__path

  def get_len(self):
    return len(self.__lines)

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("Argument Error")
    sys.exit(1)
  else:
    src = Src(args[1])
    src.print_src()
    print(src.get_line(0))
    sys.exit(0)
