# behaviorTest.hpy
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
import behavior

class BehaviorArrayTest(unittest.TestCase):
    def testIsValidPos(self):
        a = behavior.BehaviorArray()
        self.assertEquals(0, len(a._array))
        self.failIf(a.isValidPos(-1))
        self.failIf(a.isValidPos(0))
        self.failIf(a.isValidPos(1))

        a._array.insert(0, 1)
        self.assertEquals(1, len(a._array))
        self.failIf(a.isValidPos(-1))
        self.assert_(a.isValidPos(0))
        self.failIf(a.isValidPos(1))

if __name__ == '__main__':
    unittest.main()
