#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

users = []
movies = []
avgRating = 0.0

userRatings = open('defUserRatings.txt','r')
movieRatings = open('defMovieRatings.txt', 'r')

def CreateCache():
  for line in userRatings:
    row = [x.strip() for x in line.split(',')]
    users.append([int(row[0]), float(row[1])])
  print users  
  for line in movieRatings:
    if line.find(':') != -1:
      line.strip() 
      avgRating = float(line.lstrip(':'))
    else: 
      row = [x.strip() for x in line.split(',')]
      movies.append(float(row[1]))
  print movies
  
def PredictRating(user, movie):
  userRating = 0.0
  movieRating = 0.0
  for i in users:
    if i[0] == user:
      userRating = i[1]
      break;
  else:
    userRating = avgRating
  finally:
    movieRating = movies[movie]    
  return (movieRating + userRating) / 2.0