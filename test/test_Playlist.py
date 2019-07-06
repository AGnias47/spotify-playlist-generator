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
from src.Track import Track
import unittest


class test_Playlist(unittest.TestCase) :
	def setUp(self) :
		self.newPlaylist = Playlist("A new playlist test instance")

	def test_name(self) :
		self.assertEqual(self.newPlaylist.name(), "A new playlist test instance")

	def test_id(self) :
		self.assertEqual(self.newPlaylist.id(), None)

	def test_tracks(self) :
		self.assertEqual(self.newPlaylist.tracks(), None)

	def test_url(self) :
		if self.newPlaylist.id() is not None :
			self.assertEqual(self.newPlaylist.url(), "https://api.spotify.com/v1/playlists/" + self.newPlaylist.id())
		else :
			self.assertEqual(self.newPlaylist.url(), None)

	def test_set_name(self) :
		self.newPlaylist.set_name("Playlist Name Change")
		self.assertEqual(self.newPlaylist.name(), "Playlist Name Change")

	def test_set_id(self) :
		self.newPlaylist.set_id("00001")
		self.assertEqual(self.newPlaylist.id(), "00001")

	def test_set_tracks(self) :
		self.newPlaylist.set_tracks(Track("EARFQUAKE", "Tyler, The Creator"))
		self.assertEqual(self.newPlaylist.tracks().song(), "EARFQUAKE")
		self.assertEqual(self.newPlaylist.tracks().artist(), "Tyler, The Creator")


if __name__ == "__main__" :
	unittest.main()
