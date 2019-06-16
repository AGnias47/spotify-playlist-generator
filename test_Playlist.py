#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from Playlist import *
from sys import argv as arg
from sys import exit as sys_exit
import unittest

class test_Playlist(unittest.TestCase) :

	def start(self, OAUTH_token) :
		self.newPlaylist = Playlist("A new playlist test instance", OAUTH_token)

	def test_name(self) :
		self.assertEqual(Playlist.name(), "A new playlist test instance")

	def test_oauth(self) :
		self.assertEqual(Playlist.oauth(), OAUTH_token)

	def test_id(self) :
		pass
		#self.assertEqual(Playlist.id(), get id here)

	def test_tracks(self) :
		pass

	def test_setTracks(self, Tracks) :
		pass

	def test_url(self) :
		self.assertEqual(Playlist.url(), "https://api.spotify.com/v1/playlists/" + self._id)

	def test_setOAuth(self, OAUTH) :
		pass

	def test_exists(self) :
		self.assertEqual(newPlaylist.exists(Playlist.oauth(), Playlist.url()), True)

	def test_delete(self) :
		pass

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	unittest.main()
	#Need to put more work into picking up an existing playlist for this to work well
	#existingPlaylist = Playlist("Musical", OAUTH_token, None, None)
