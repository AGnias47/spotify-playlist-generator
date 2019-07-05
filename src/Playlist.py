#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
from spotify_playlist_module import *


class Playlist :
	def __init__(self, oauth=None, name="Unnamed Playlist", tracks=None, ID=None) :
		self._name = name
		self._oauth = oauth
		self._tracks = tracks
		self._id = ID
		if self._id is not None :
			self._url = "https://api.spotify.com/v1/playlists/" + self._id
		else :
			self._url = None

	def name(self) :
		return self._name

	def oauth(self) :
		return self._oauth

	def tracks(self) :
		return self._tracks

	def id(self) :
		return self._id

	def url(self) :
		return self._url

	def setTracks(self, Tracks) :
		self._tracks = Tracks

	def setOAuth(self, OAUTH) :
		self._oauth = OAUTH

	def setID(self, ID) :
		self._id = ID

	def spotifyInit(self) :
		print(self._oauth, self._name, "Playlist generated from Spotify API")
		(self._id, self._url) = create_playlist(self._oauth, self._name, "Playlist generated from Spotify API")
		if self._id is not None and self._url is not None :
			return True
		else : 
			return False

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
