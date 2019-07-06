#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("..")
path.append("src")


from src.Track import Track
import unittest


class test_Track(unittest.TestCase) :
	def setUp(self) :
		self.newTrack = Track("Born to Run", "Bruce Springsteen")
		self.newSpotifyTrack = Track("Interplay", "Bill Evans", "fake/href", "fake/externalURL")

	def test_song(self) :
		self.assertEqual(self.newTrack.song(), "Born to Run")

	def test_artist(self) :
		self.assertEqual(self.newTrack.artist(), "Bruce Springsteen")

	def test_href(self) :
		self.assertEqual(self.newSpotifyTrack.href(), "fake/href")

	def test_external_url(self) :
		self.assertEqual(self.newSpotifyTrack.external_url(), "fake/externalURL")

	def test_set_song(self) :
		self.newTrack.set_song("XXX")
		self.assertEqual(self.newTrack.song(), "XXX")

	def test_set_artist(self) :
		self.newTrack.set_artist("Kendrick Lamar")
		self.assertEqual(self.newTrack.artist(), "Kendrick Lamar")

	def test_set_href(self) :
		self.newTrack.set_href("href/Bruce")
		self.assertEqual(self.newTrack.href(), "href/Bruce")

	def test_set_external_url(self) :
		self.newSpotifyTrack.set_external_url("fake/morefake/externalURL")
		self.assertEqual(self.newSpotifyTrack.external_url(), "fake/morefake/externalURL")

if __name__ == "__main__" :
	unittest.main()
