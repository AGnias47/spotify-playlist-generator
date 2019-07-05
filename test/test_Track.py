#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

import sys
sys.path.append("..")

from src.Track import Track
import unittest


class test_Track(unittest.TestCase) :
	def setUp(self) :
		self.newTrack = Track("Born to Run", "Bruce Springsteen")

	def test_song(self) :
		self.assertEqual(self.newTrack.song(), "Born to Run")

	def test_artist(self) :
		self.assertEqual(self.newTrack.artist(), "Bruce Springsteen")

	def test_set_song(self) :
		self.newTrack.set_song("XXX")
		self.assertEqual(self.newTrack.song(), "XXX")

	def test_set_artist(self) :
		self.newTrack.set_artist("Kendrick Lamar")
		self.assertEqual(self.newTrack.artist(), "Kendrick Lamar")


if __name__ == "__main__" :
	unittest.main()
