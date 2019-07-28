#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.Artist import Artist
import unittest


class test_Artist(unittest.TestCase) :
	def setUp(self) :
		self.newArtist = Artist("Kendrick Lamar")

	def test_name(self) :
		self.assertEqual(self.newArtist.name(), "Kendrick Lamar")

	def test_external_url(self) :
		self.assertEqual(self.newArtist.external_url(), None)

	def test_id(self) :
		self.assertEqual(self.newArtist.id(), None)

if __name__ == "__main__" :
	unittest.main()
