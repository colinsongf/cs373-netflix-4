#!/usr/bin/env python

# ------------------------------
# projects/Netflix/RunNetflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# -------------------------------

"""
To run the program
    % python RunNetflix.py < RunNetflix.in > RunNetflix.out
    % chmod ugo+x RunNetflix.py
    % RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
    % pydoc -w Netflix
"""

# -------
# imports
# -------

import sys
import math

from Netflix import CreateCache, Netflix

movieRatings = 'defMovieRatings.txt'
userRatings = 'defUserRatings.txt'
# ----
# main
# ----

CreateCache(userRatings,movieRatings)
Netflix(sys.stdin, sys.stdout)