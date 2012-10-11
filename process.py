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
movieRatingsByYear = open('movieRatingsByYear.txt','w')
retrievedDict = {}
userRatings = {}
movieDict = {}
movieYears = {}



def findRatings(movieTitle, user):
  fileName = "mv_00"+"0"*(5-movieTitle.__len__())+movieTitle+".txt"
  fileDir = "/u/downing/cs/netflix/training_set/"+fileName
  trainingFile = open(fileDir,'r')
  print "finding ratings for: "+fileName+"\n"
  for line in trainingFile:
    if line.find(':') == -1:
      row = [x.strip() for x in line.split(',')]
      if row[0].find(user) != -1:
        retrievedDict[row[0]] = float(row[1])
	#print retrievedDict

def getYear(movieID):
  return movieDict[movieID]
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
  numOfAllRatings = 0
  for filename in sys.argv[1:]:
    print filename
    with open(filename) as training:
      totalRatings = 0.0
      numOfRatings = 0
      for line in training:
        if line.find(':') != -1:
          movieId = line.strip()
        if line.find(':') == -1:
          numOfRatings += 1
          row = [x.strip() for x in line.split(',')]
          ProcessUser(row[0],row[1]);
          totalRatings += int(row[1]) 
      avgRating = totalRatings/numOfRatings
      totalAverage += totalRatings
      numOfAllRatings += numOfRatings
      ratings.write(movieId.rstrip(':')+","+str(avgRating)+","+movieDict[movieId.rstrip(':')]+"\n")
  totalAverage /= numOfAllRatings
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
    if line.find(':') != -1:
      movie = line[:-2]
      #findRatings(movie)
    else:
      findRatings(movie,line.strip())
      #print str(line.strip())
      probeAnswers.write(str(retrievedDict[line.strip()])+"\n")
      
def ProcessMovies():
  i = 0
  for line in movies:
    row = [x.strip() for x in line.split(',')]
    movieDict[row[0]] = row[1]    

def ProcessMovieYears():
  for i in range(1890, 2010, 5):
    movieYears[i] = [0,0]
  ratings = open('defMovieRatings.txt', 'r')
  for line in ratings:
    if line.find(":") == -1:
      row = [x.strip() for x in line.split(',')]
     # print row
      if movieDict[row[0]].find('NULL') == -1:
        yearDiff = int(movieDict[row[0]]) % 5
        yearKey = int(movieDict[row[0]]) - yearDiff
        #add rating to designated year range
        movieYears[yearKey][0] += float(row[1])
        #inc num of ratings for year range
        movieYears[yearKey][1] += 1
  for i in movieYears:
    average = 0.0
    #divide by zero check
    if (movieYears[i][1] != 0.0):
      average = movieYears[i][0]/movieYears[i][1]
    movieRatingsByYear.write(str(i)+","+str(average)+"\n")
