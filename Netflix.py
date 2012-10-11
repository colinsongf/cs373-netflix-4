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
  #print avgRating
  #print yearlyRatings

def getYearRating(movie):
  #print yearlyRatings
  #print movies[movie-1][1]
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
  movieRating = movies[movie-1][0]
  averageYearRating = getYearRating(movie)
  if user in users:
    userRating = users[user]
    rating = UserRating
    
  else:
    rating = avgRating
  movieRating = movies[movie-1][0]
  return rating
  #return round(float((movieRating + userRating) / 2.0))
    '''#userRating = users[user]
    #userOffset = userRating*.9
    #movieOffset = movieRating*.1
    #userRating = avgRating + userRating - movieRating
    userRating = userRating*.9 + users[user]*.1
    #userRating = 0.8*userRating+0.2*movieRating
    #userRating = float((movieRating +userRating) / 2.0)
    
    if (userRating < avgRating < movieRating):
      userRating += (movieRating - avgRating)
      #userRating = 0.3*userRating+0.7*movieRating
      #userRating = round(userRating)
      return userRating
    elif (userRating > avgRating > movieRating):
      userRating -= (avgRating - movieRating)
      #userRating = 0.3*userRating+0.7*movieRating
      #userRating = round(userRating)
      return userRating
    return userRating
  else:    
    userRating = movieRating
    return userRating
    #userRating = midpoint(userRating, movieRating)
  #movieRating = movies[movie-1][0]
  #return float((movieRating + averageYearRating + userRating) / 3.0)
  #return 0.0'''
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
