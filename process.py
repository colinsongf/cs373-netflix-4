#!/usr/bin/env python
"""
process through given files to produce cache docs
"""
import sys

userAvgRatings = {};

f = open('mv_0002043.txt', 'r')
for line in f:
  if line.find(':') != -1:
    print line
  else:
    print [x.strip() for x in line.split(',')]
