#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

import spotify_module
from sys import argv as arg
from sys import exit as sys_exit

class Playlist :
	def __init__(self, name, oauth=None, tracks=None, ID=None) :
		self._name = name
		self._oauth = oauth
		self._tracks = tracks
		self._id = ID

	def create(self) :
		if self._oauth is not None and id is None :
			(self._id, URL) = spotify_module.create_playlist(self._oauth, self._name)
			#self.setID(ID)
		return self.exists(self._oauth)

	def name(self) :
		return self._name

	def oauth(self) :
		return self._oauth

	def setOAuth(self, OAUTH) :
		self._oauth = OAUTH

	def setID(self, ID) :
		self._id = ID

	def tracks(self) :
		return self._tracks

	def setTracks(self, Tracks) :
		self._tracks = Tracks

	def id(self) :
		return self._id

	def url(self) :
		return "https://api.spotify.com/v1/playlists/" + self._id

	def exists(self, oauth) :
		return spotify_module.check_existence(oauth, self.url())

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	playlist = Playlist("Doldrums", OAUTH_token)
	playlist.create()
	print(playlist.name())
	print(playlist.id())
