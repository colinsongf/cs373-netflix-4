'''
Created on Sep 23, 2012

@author: Administrator
'''
#!/usr/bin/env python

# -------------------------------
# projects/Netflix/TestNetflix.py
# Copyright (C) 2012
# Thomas Preli & Newman Willis
# -------------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.py.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import CreateCache, PredictRating, Netflix, getUsers, getMovies, getRatings 

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :

    # ----
    # CreateCache
    # ----
    
    def test_CreateCache_1(self):
        CreateCache('ZU1.txt', 'ZM1.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 2
        testMovies[0] = prototypeMovies[0]
        testMovies[1] = prototypeMovies[1]
        actualUsers = {'1' : 5.0, '2': 3.0}
        actualMovies = [5.0, 1.0]
        print testMovies
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)
        
    def test_CreateCache_2(self):
        CreateCache('ZU2.txt', 'ZM2.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 4
        testMovies[0] = round(prototypeMovies[0])
        testMovies[1] = round(prototypeMovies[1])
        testMovies[2] = round(prototypeMovies[2])
        testMovies[3] = round(prototypeMovies[3])
        actualUsers = {'1' : 5.0, '10034': 4.0, '2': 3.0, '8901267': 3.0}
        actualMovies = [4.0, 3.0, 4.0, 4.0]
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)
        
    def test_CreateCache_3(self):
        CreateCache('ZU3.txt', 'ZM3.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 4
        testMovies[0] = round(prototypeMovies[0])
        testMovies[1] = round(prototypeMovies[1])
        testMovies[2] = round(prototypeMovies[2])
        testMovies[3] = round(prototypeMovies[3])
        actualUsers = {'1' : 5.0, '10034': 4.0, '2': 3.0, '8901267': 3.0}
        actualMovies = [4.0, 3.0, 4.0, 4.0]
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)

    # ----
    # PredictRating
    # ----
            
    def test_PredictRating_1(self):
        userID = '1'
        movieID = 2
        testRating = round(PredictRating(userID, movieID), 2)
        actualRating = 3.46;
        self.assert_(testRating == actualRating)
        
    def test_PredictRating_2(self):
        userID = '10034'
        movieID = 3
        testRating = round(PredictRating(userID, movieID), 2)
        actualRating = 4.64;
        self.assert_(testRating == actualRating)
        
    def test_PredictRating_3(self):
        userID = '17'
        movieID = 1
        testRating = round(PredictRating(userID, movieID), 2)
        actualRating = 0.0;
        self.assert_(testRating == actualRating)
       
    # ----
    # Netflix
    # ----        
    
    def test_Netflix_1(self):
      r = StringIO.StringIO("1:\n1\n87")
      w = StringIO.StringIO() 
      Netflix(r, w)
      actualRatings = [5, 0]
      self.assert_(getRatings() == actualRatings)

    def test_Netflix_2(self):
      r = StringIO.StringIO("2:\n1\n999232")
      w = StringIO.StringIO() 
      Netflix(r, w)
      actualRatings = [5, 0 , 3.4608600264852694, 0]
      self.assert_(getRatings() == actualRatings)
         
    def test_Netflix_3(self):
      r = StringIO.StringIO("4:\n2")
      w = StringIO.StringIO() 
      Netflix(r, w)
      actualRatings = [5, 0 , 3.4608600264852694, 0, 0]
      self.assert_(getRatings() == actualRatings)
  

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
