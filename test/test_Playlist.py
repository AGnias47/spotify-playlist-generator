#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("..")
path.append("../src")

from src.Playlist import Playlist
import unittest


class test_Playlist(unittest.TestCase) :
	def setUp(self) :
		self.newPlaylist = Playlist("A new playlist test instance")

	def test_name(self) :
		self.assertEqual(self.newPlaylist.name(), "A new playlist test instance")

	def test_id(self) :
		self.assertEqual(self.newPlaylist.id(), None)

	def test_tracks(self) :
		self.assertEqual(self.newPlaylist.id(), None)

	def test_url(self) :
		if self.newPlaylist.id() is not None :
			self.assertEqual(self.newPlaylist.url(), "https://api.spotify.com/v1/playlists/" + self.newPlaylist.id())
		else :
			self.assertEqual(self.newPlaylist.url(), None)


if __name__ == "__main__" :
	unittest.main()
