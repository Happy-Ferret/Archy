# platform_specificTest.py
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

import testUtil
import unittest
import platform_specific

class platform_specificTest(unittest.TestCase):
    def testInitialization(self):
        ini_msg = "Probably platform_specific is initialized before pygame"
        self.assert_(platform_specific.Command_Key, ini_msg)
        self.assert_(platform_specific.LEAP_Forward_Key, ini_msg)
        self.assert_(platform_specific.LEAP_Backward_Key, ini_msg)

if __name__ == '__main__':
    unittest.main()
