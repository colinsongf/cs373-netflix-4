#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------
import math
import sys
ratings = []

def sqre_diff (x, y) :
  return (x - y) ** 2

def ReadOutput(results):
  for line in results:
    if line.find(':') == -1:
      #print line[:-1].strip()
      ratings.append(line[:-1].strip())
  print str(RMSE(open("probeAnswers.txt"),ratings))

def RMSE(probeAns, ratings):
  probeAnswers = []
  total = 0.0
  i =0
  for line in probeAns:
    print line
    if line.find(':') == -1:
      print line[:-1]
      total += sqre_diff(ratings[i],float(line[:-1]))
      i+=1
  s = len(ratings)
  #v = sum(map(sqre_diff, probeAnswers, ratings), 0.0)
  return math.sqrt(total / s)
