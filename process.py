#!/usr/bin/env python
"""
Process through given files to produce cache docs
Average user rating 3.7
"""
import sys

userAvgRatings = {}
numOfMovies = 0

#training = open('mv_0002043.txt', 'r')
movies = open('movie_titles.txt','r')
users = open('defUserRatings.txt','w')
ratings = open('defMovieRatings.txt', 'w')
userRatings = []

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
    with open(filename) as training:
      for line in training:
        if line.find(':') != -1:
          movieId = line.strip()
        if line.find(':') == -1:
          numOfRatings += 1
          row = [x.strip() for x in line.split(',')]
          ProcessUser(row[0],row[1]);
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
  for i in userRatings:
    if(i[0] == user):
      i[1] += rating
      i[2] += 1                                  
      break
  else:
    userRatings.append([int(user),int(rating),1.0])

def writeUsers():
  avg = 0.0
  for i in userRatings:
    avg = i[1]/i[2]
    users.write(str(i[0])+","+str(avg)+"\n")