#!/usr/bin/env python
"""
process through given files to produce cache docs
average user rating 3.7
"""
import sys

userAvgRatings = {}
numOfMovies = 0
numOfRatings = 0
totalRatings = 0.0
avgRating = 0.0
training = open('mv_0002043.txt', 'r')
movies = open('movie_titles.txt','r')

for line in training:
  if line.find(':') != -1:
    numOfMovies += 1
    print line.strip()
  else:
    numOfRatings += 1
    row = [x.strip() for x in line.split(',')]
    totalRatings += int(row[1])  
avgRating = totalRatings/numOfRatings
print avgRating

for line in movies:
  row = [x.strip() for x in line.split(',')]
  print row[0] + " "+ str(3.77)
