# audioTest.py
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
from audio import *

class NullSoundTest(unittest.TestCase):
    def testNothingHappens(self):
        sound = NullSound()
        sound.set_volume(None)
        sound.stop()
        sound.play()

class MusicSoundTest(unittest.TestCase):
    def test__init__(self):
        name = "Sample Name"
        sound = MusicSound(name)
        self.assertEquals(name, sound.soundName)

if __name__ == '__main__':
    unittest.main()
