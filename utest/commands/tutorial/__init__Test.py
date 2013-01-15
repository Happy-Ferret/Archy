# __init__Test.py
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
import unittest
import utest.testUtil
from commands.tutorial import *

class ExampleParserTest(unittest.TestCase):
    def testCreate(self):
        ex1 = ExampleParser('ex1.txt')
        self.assertEqual('EX1', ex1.name)
        self.assertEqual('ex1.ogg', ex1.sound)
        self.assert_(ex1.title.startswith('EX1'))
        self.assertEqual('', ex1.text)
        self.assertEqual('300,-300', ex1.boardPos)
        self.assertEqual('', ex1.script[0])
        self.assertEqual('00.00\tscroll\t-10', ex1.script[1])
        self.assert_(ex1.soundtrack)
        self.assert_(ex1.original_command_history_length >= 0)
        

if __name__ == '__main__':
    unittest.main()
