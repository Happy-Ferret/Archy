# quitTest.py
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
from commands.quit import *

class QuitCommandTest(unittest.TestCase):
    def testBasics(self):
        command = QuitCommand()
        self.assertEqual("QUIT", command.name())
        self.failIf(command.recordable())

if __name__ == '__main__':
    unittest.main()
