#! /usr/bin/python
# utest.py
# The Raskin Center for Humane Interfaces (RCHI) 2005

# This work is licensed under the Creative Commons
# Attribution-NonCommercial-ShareAlike License. To view 
# a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/2.0/ 

# or send a letter to :

# Creative Commons
# 559 Nathan Abbott Way
# Stanford, California 94305, 
# USA.
# --- --- ---

# Runs specified Archy unit test.
# If no parameters is specified runs all unit tests in "utest" package -
# tests found under "utest" directory and subdirectories.
# Unit test file is considered a .py file which has name ending on "Test"
# (case is important)

import utest.run_tests

utest.run_tests.run()

