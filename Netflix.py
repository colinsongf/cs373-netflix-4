#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

import math
import sys
import re

users = {}
movies = [[0,0] for v in xrange(17770)]
avgRating = 0.0
ratings = []
retrievedRatings = []
retrievedDict = {}
yearlyRatings = {}
moviesByYear = {}

###
# creates the cache for predicting the data from the stored
###
def CreateCache(userFile, movieFile):
  global avgRating
  userRatings = open(userFile,'r')
  movieRatings = open(movieFile, 'r')
  for line in userRatings:
    row = [x.strip() for x in line.split(',')]
    users[row[0]] = float(row[1])
  for line in movieRatings:
    if line.find(':') != -1:
      line.strip()
      avgRating = float(line.lstrip(':'))
    else:
      row = [x.strip() for x in line.split(',')]
      movies[int(row[0])-1][0] = float(row[1])
      movies[int(row[0])-1][1] = row[2]

###
# method for predicting the data
# currently implements a generic way to predict rating. Averages the movies
# average rating and the users average rating.
###
def PredictRating(user, movie):
  userRating = 0.0
  prediction = 0.0
  movieRating = movies[movie-1][0]
  if user in users:
    userRating = users[user]
    prediction = avgRating + (movieRating - avgRating) +(userRating - movieRating)
    prediction *= (movieRating/avgRating)
    if(prediction > 5):
      prediction = 5
    elif(prediction < 0):
      prediction = 0
  return prediction

###
# method that process input txt file and calculate predictions
###
def Netflix(r,w):
  movie = 0
  results = ""
  for line in r:
    #print line.strip()
    if line.find(':') != -1:
      #line = re.search(r'\d\.\d*E[+-]\d+',line[0]).group
      movie = int(line[:-2].strip('\xef\xbb\xbf\r\n: '))
      results += line
    else:
      if line.strip() != "":
        rating = PredictRating(line[:-1],movie)
        results += str(rating)+"\n"
        ratings.append(rating)
      else:
      	results +="\n" 
  print results

# simple functions to help with testing
def getMovies():
    return movies
    
def getUsers():
    return users 
