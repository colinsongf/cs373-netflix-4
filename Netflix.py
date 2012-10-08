#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

users = {}
movies = [0]*17770
avgRating = 0.0
ratings = []

"""
creates the cache for predicting the data from the stored 
"""
def CreateCache(userFile, movieFile):
  userRatings = open(userFile,'r')
  movieRatings = open(movieFile, 'r')
  for line in userRatings:
    row = [x.strip() for x in line.split(',')]
    #print row
    users[row[0]] = float(row[1])  
  for line in movieRatings:
    if line.find(':') != -1:
      line.strip() 
      avgRating = float(line.lstrip(':'))
    else: 
      row = [x.strip() for x in line.split(',')]
      movies[int(row[0])-1] = float(row[1])

"""
method for predicting the data
currently implements a generic way to predict rating. Averages the movies
average rating and the users average rating.
"""
def PredictRating(user, movie):
  userRating = 0.0
  movieRating = 0.0
  if user in users:
    userRating = user[user]
  else:
    #set default rating for small test cases
    #userRating = 3.77
    userRating = avgRating
  #def movie rating purely for testing read
  movieRating = movies[movie-1]
  #movieRating = 3.6672
  return float((movieRating + userRating) / 2.0)

def Netflix(r,w):
  movie = 0
  for line in r:
    if line.find(':') != -1:
      movie = int(line[:-2])
      ratings.append(str(movie)+":")
      print str(movie)+":"
    else:
      ratings.append(PredictRating(int(line[:-1]),movie))
      #print PredictRating(int(line[:-1]),movie)
  print ratings
  #RMS(ratings)
