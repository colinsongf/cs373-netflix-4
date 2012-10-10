#!/usr/bin/env python
"""
Process through given files to produce cache docs
Average user rating 3.7
"""
import sys

userAvgRatings = []
numOfMovies = 0

#training = open('mv_0002043.txt', 'r')
movies = open('movie_titles.txt','r')
probe = open('probe.txt', 'r')
users = open('defUserRatings.txt','w')
ratings = open('defMovieRatings.txt', 'w')
probeAnswers = open('probeAnswers.txt','w')
retrievedDict = {}
userRatings = {}

def findRatings(movieTitle):
	fileName = "mv_00"+"0"*(5-movieTitle.__len__())+movieTitle+".txt"
	fileDir = "/u/downing/cs/netflix/training_set/"+fileName
	trainingFile = open(fileDir,'r')
	print fileName
	for line in trainingFile:
		if line.find(':') == -1:
			row = [x.strip() for x in line.split(',')]
			retrievedDict[row[0]] = float(row[1])

"""
Reads the training data file and assigns the given rating as
the default rating for the given users. Then calculates the average
rating for training movie for use in the average movie rating.
Outputs to defUsers.txt. Might think about inorporating year into this
later
"""
def ProcessTraining():
  numOfRatings = 0
  totalRatings = 0.0
  avgRating = 0.0
  numOfMovies = 0
  totalAverage = 0.0
  movieId = ""
  for filename in sys.argv[1:]:
    numOfMovies += 1
    print filename
    with open(filename) as training:
      for line in training:
        if line.find(':') != -1:
          movieId = line.strip()
        if line.find(':') == -1:
          numOfRatings += 1
          row = [x.strip() for x in line.split(',')]
          ProcessUser(row[0],row[1]);
          #probeAnswers.write(row[1]+"\n")
          totalRatings += int(row[1]) 
      avgRating = totalRatings/numOfRatings
      totalAverage += avgRating
      ratings.write(movieId.rstrip(':')+","+str(avgRating)+"\n")
  totalAverage /= 17770
  ratings.write(':'+str(totalAverage));
  writeUsers()

"""
Checks for user in userRatings, if not found appends. Used for calculating 
averages of specific users
"""
def ProcessUser(user,rating):
  if user in userRatings:
    userRatings[user][0] += float(rating)
    userRatings[user][1] += 1.0
  else:
    userRatings[user] = [float(rating), 1.0]

def writeUsers():
  avg = 0.0
  for i in userRatings:
    avg = float(userRatings[i][0])/userRatings[i][1]
    users.write(str(i)+","+str(avg)+"\n")

def ProcessProbe():
  for line in probe:
    if line.fine(':') != -1:
      movie = line[:-2]
      findRatings(movie)
    else:
      probeAnswers.write(str(retrievedDict[line:-1])+"\n")
