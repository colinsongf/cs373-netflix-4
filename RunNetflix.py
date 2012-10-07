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

from Netflix import CreateCache

# ----
# main
# ----

CreateCache()