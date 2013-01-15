# keyboardTest.py
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
from commands.tutorial.keyboard import *

class KeyboardTest(unittest.TestCase):
    def testInitialization(self):
        self.assert_(visible() >= 0)

    def testShowHide(self):
        hide()
        self.failIf(visible())
        self.assertEqual('', shownKey())
        
        sampleKey = 'Sample Key'

        show(sampleKey)
        self.assert_(visible())
        self.assertEqual(sampleKey, shownKey())

        hide()
        self.failIf(visible())
        self.assertEqual('', shownKey())
        
        show()
        self.assert_(visible())
        self.assertEqual('', shownKey())


if __name__ == '__main__':
    unittest.main()
