#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

import math

users = {}
movies = [[0,0] for v in xrange(17770)]
avgRating = 0.0
ratings = []
retrievedRatings = []
retrievedDict = {}
yearlyRatings = {}
moviesByYear = {}
"""
creates the cache for predicting the data from the stored 
"""
def CreateCache(userFile, movieFile, yearRatings):
  global avgRating
  userRatings = open(userFile,'r')
  movieRatings = open(movieFile, 'r')
  ratingsByYear = open(yearRatings,'r')
  for line in userRatings:
    row = [x.strip() for x in line.split(',')]
    users[row[0]] = float(row[1])
  for line in movieRatings:
    if line.find(':') != -1:
      line.strip() 
      avgRating = float(line.lstrip(':'))
    else: 
      row = [x.strip() for x in line.split(',')]
      #print movies
      #print row
      movies[int(row[0])-1][0] = float(row[1])
      movies[int(row[0])-1][1] = row[2]
  #print movies
  for line in ratingsByYear:
    row = [x.strip() for x in line.split(',')]
    yearlyRatings[row[0]] = float(row[1].strip())

def getYearRating(movie):
  movieYear = movies[movie-1][1]
  if(movieYear != 'NULL'):
    year = int(movieYear) 
    yearInterval = year-(year%5)
    return yearlyRatings[str(yearInterval)]
  else:
    return 0.0

"""
method for predicting the data
currently implements a generic way to predict rating. Averages the movies
average rating and the users average rating.
"""
def PredictRating(user, movie):
  userRating = 0.0
  rating = 0.0
  movieRating = movies[movie-1][0]
  #averageYearRating = getYearRating(movie)
  if user in users:
    userRating = users[user]
    userOffset = avgRating/userRating
    movieOffset = avgRating/movieRating
    #rating = avgRating + userRating*userOffset - movieRating*movieOffset
    rating = avgRating + userRating**(movieRating/userRating)
  else:    
    userRating = movieRating
    rating = userRating
    #userRating = midpoint(userRating, movieRating)
  #movieRating = movies[movie-1][0]
  #return float((movieRating + averageYearRating + userRating) / 3.0)
  return rating
"""
method that process input txt file and calculate predictions
"""
def Netflix(r,w):
  movie = 0
  results = ""
  for line in r:
    if line.find(':') != -1:
      movie = int(line[:-2])
      results += line
    else:
      rating = PredictRating(line[:-1],movie)
      #results += str(movies[movie-1][0])+" "+str(rating)+" "+str(avgRating)+"\n"
      results += str(rating)+"\n"
      ratings.append(rating)
  print results.strip()

#simple functions to help with testing  
def getMovies():
    return movies
    
def getUsers(): 
    return users     
