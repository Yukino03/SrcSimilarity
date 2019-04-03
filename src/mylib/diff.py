#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy

def cmp_src(src1, src2):
  '''[Public]read tokens sequently'''
  dic1 = word_count(src1)
  dic2 = word_count(src2)
  dic1 = extract_alph(dic1)
  dic2 = extract_alph(dic2)
  list1 = sort_dic(dic1)
  list2 = sort_dic(dic2)
  compare(list1, list2)
  match_rate(list1, list2)
  # print("----list1----")
  # for x in list1:
  #   print(x)
  # print("----list2----")
  # for y in list2:
  #   print(y)

def compare(list1, list2):
  '''[Private]receive list of tuple(String, Integer)'''
  unmatch = []
  unmatch2 = copy.deepcopy(list2)
  print("[Matched]")
  for line1 in list1:
    flag = True
    for line2 in list2:
      if line1[0] == line2[0]:
        # mutch!!
        message = str(line1) + "   ->   " + str(line2)
        unmatch2.pop(unmatch2.index(line2))
        # escape list2 loop
        flag = False
        break
    if flag == True:
      unmatch.append(line1)
    else:
      print(message)
  print("\n","[Source1 only]")
  for line3 in unmatch:
    print(line3,"   ->")
  print("\n","[Source2 only]")
  for line4 in unmatch2:
    print("->   ",line4)


def extract_alph(dic):
  '''[Private]Extract alphabet from token dict'''
  alp_dic = {}
  for key in dic.keys():
    if isname(key):
      alp_dic[key] = dic[key]
  return alp_dic

def word_count(src1):
  '''[Private]'''
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
  '''[Private]tupleのlistを返す'''
  dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse = True)
  return dic_sorted

def match_rate(list1, list2):
  '''[Private]一致率を求める'''
  # 出現tokenの一致率
  # 出現数の変化
  match_num = 0
  unmatch = []
  unmatch2 = copy.deepcopy(list2)
  for line1 in list1:
    flag = True
    for line2 in list2:
      if line1[0] == line2[0]:
        # mutch!!
        match_num = match_num + 1
        # message = str(line1) + "   ->   " + str(line2)
        unmatch2.pop(unmatch2.index(line2))
        # escape list2 loop
        flag = False
        break
    if flag == True:
      unmatch.append(line1)
  print("合致数=",match_num)
  print("src1_only=",len(unmatch))
  print("src2_only=",len(unmatch2))

def isname(string):
  '''[Private]コメントや記号類を弾く'''
  if str.isalpha(string[0]):
    return True
  elif str.isdigit(string[0]):
    return False
