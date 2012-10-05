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

from Netflix import Netflix_read_parameters, Netflix_read_node, Netflix_no_prereqs, Netflix_remove_tasks, Netflix_eval, Netflix_print, Netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    # ----
    # read_parameters
    # ----

    def test_read_parameters_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = Netflix_read_parameters(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

        
    # ----    
    # read_node    
    # ----
        
    def test_read_node_1 (self) :
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        a = [5, 4]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        Netflix_read_node(r, a, cache)
        self.assert_(cache[3][1] == 1)
        self.assert_(cache[3][5] == 1)
        self.assert_(cache[2][5] == 1)
        self.assert_(cache[2][3] == 1)
        self.assert_(cache[4][3] == 1)
        self.assert_(cache[5][1] == 1)

        
    # ----
    # no_prereqs
    # ----
    
    def test_no_prereqs_1 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        v = Netflix_no_prereqs(1, 5, cache)
        self.assert_(v)             
 
        
    # ----
    # remove_tasks
    # ----
    
    def test_remove_tasks_1 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        Netflix_remove_tasks(1, 5, cache)
        self.assert_(cache[1][1] == 0)
        self.assert_(cache[2][1] == 0)
        self.assert_(cache[3][1] == 0)
        self.assert_(cache[4][1] == 0)
        self.assert_(cache[5][1] == 0)           
        
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        a = [5, 4]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        Netflix_read_node(r, a, cache)
        v = Netflix_eval(a[0], cache)
        self.assert_(v[0] == 1)
        self.assert_(v[1] == 5)
        self.assert_(v[2] == 3)
        self.assert_(v[3] == 2)
        self.assert_(v[4] == 4)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        Netflix_print(w, (1, 3, 4, 5, 2))
        self.assert_(w.getvalue() == "1 3 4 5 2\n")
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        Netflix_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n")
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."