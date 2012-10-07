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
users = open('defUsers.txt','w')
ratings = open('defRatings.txt', 'w')

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
  for filename in sys.argv[1:]:
    with open(filename) as training:
      for line in training:
        if line.find(':') == -1:
          numOfRatings += 1
          row = [x.strip() for x in line.split(',')]
          users.write(row[0]+","+row[1]+"\n")
          totalRatings += int(row[1])  
  avgRating = totalRatings/numOfRatings


"""
Reads the movie data file and writes the average rating calculated
previously as the default rating for all movies. Outpust to defRatings.txt.
"""
def ProcessMovies():
  for line in movies:
    row = [x.strip() for x in line.split(',')]
    ratings.write(row[0]+","+str(avgRating)+","+row[1]+"\n")

