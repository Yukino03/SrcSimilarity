#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cmp_src(src1, src2):
  '''read tokens sequently'''
  dic1 = word_count(src1)
  dic2 = word_count(src2)
  dic1 = extract_alph(dic1)
  dic2 = extract_alph(dic2)
  list1 = sort_dic(dic1)
  list2 = sort_dic(dic2)
  print("DEBUG","list1")
  for x in list1:
    print(x)
  print("DEBUG","list2")
  for y in list2:
    print(y)

def extract_alph(dic):
  '''Extract alphabet from token dict'''
  alp_dic = {}
  for key in dic.keys():
    if isname(key):
      alp_dic[key] = dic[key]
  return alp_dic

def word_count(src1):
  dic = {}
  for x in range(len(src1)):
    line = src1.tokenize(x)
    for token in line:
      if token in dic:
        dic[token] = dic[token]+1
      else :
        dic[token] = 1
  return dic

def sort_dic(dic):
  dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse = True)
  return dic_sorted

def isname(string):
  '''コメントや記号類を弾く'''
  if str.isalpha(string[0]):
    return True
  elif str.isdigit(string[0]):
    return False
