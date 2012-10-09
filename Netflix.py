#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

import math

users = {}
movies = [0]*17770
avgRating = 0.0
ratings = []
retrievedRatings = []
retrievedDict = {}

"""
creates the cache for predicting the data from the stored 
"""
def CreateCache(userFile, movieFile):
  userRatings = open(userFile,'r')
  movieRatings = open(movieFile, 'r')
  for line in userRatings:
    row = [x.strip() for x in line.split(',')]
    users[row[0]] = round(float(row[1]),2)
  for line in movieRatings:
    if line.find(':') != -1:
      line.strip() 
      avgRating = round(float(line.lstrip(':')),2)
    else: 
      row = [x.strip() for x in line.split(',')]
      movies[int(row[0])-1] = round(float(row[1]),2)
  #print avgRating

"""
method for predicting the data
currently implements a generic way to predict rating. Averages the movies
average rating and the users average rating.
"""
def PredictRating(user, movie):
  userRating = 0.0
  movieRating = 0.0
  if user in users:
    userRating = users[user]
  else:
    userRating = avgRating
  movieRating = movies[movie-1]
  return float((movieRating + userRating) / 2.0)

def findRatings(movieTitle):
	fileName = "mv_00"+"0"*(5-movieTitle.__len__())+movieTitle+".txt"
	fileDir = "/u/downing/cs/netflix/training_set/"+fileName
	trainingFile = open(fileDir,'r')
	#print fileName
	for line in trainingFile:
		if line.find(':') == -1:
			row = [x.strip() for x in line.split(',')]
			retrievedDict[row[0]] = float(row[1])
			
def getRating(user, movieTitle):
	fileName = "mv_00"+"0"*(5-movieTitle.__len__())+movieTitle+".txt"
	fileDir = "/u/downing/cs/netflix/training_set/"+fileName
	trainingFile = open(fileDir,'r')
	print fileName
	for line in trainingFile:
		if line.find(':') == -1:
			row = [x.strip() for x in line.split(',')]
			if row[0] == user:
				retrievedDict[row[0]] = float(row[1])

def Netflix(r,w):
  movie = 0
  results = ""
  for line in r:
    if line.find(':') != -1:
      movie = int(line[:-2])
      #print str(movie)
      #findRatings(str(movie))
      #print retrievedDict
      results += line
    else:
      rating = PredictRating(line[:-1],movie)
      #retrievedRatings.append(retrievedDict[line[:-1]])
      results += str(rating)+"\n"
      ratings.append(rating)
  rmse = RMSE(open("probeAnswers.txt"),ratings)
  print rmse
  #print results.strip()
  #print retrievedRatings
  #print str(rmse)+"\n"+results.strip()
  
def sqre_diff (x, y) :
  return (x - y) ** 2

def RMSE(probeAns, ratings):
  probeAnswers = []
  total = 0.0
  i =0
  for line in probeAns:
    if line.find(':') == -1:
      #print line[:-1]
      #probeAnswers.append(float(line[:-1]))
      total += sqre_diff(ratings[i],float(line[:-1]))
      i+=1
  #print probeAnswers
  s = len(ratings)
  #v = sum(map(sqre_diff, probeAnswers, ratings), 0.0)
  return math.sqrt(total / s)

#simple functions to help with testing  
def getMovies():
    return movies
    
def getUsers(): 
    return users     
