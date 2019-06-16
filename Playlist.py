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
	def __init__(self, name, oauth=None, tracks=None, id=None) :
		self._name = name
		self._oauth = oauth
		self._tracks = tracks
		self._id = id
		if self._oauth is not None and id is None :
			(self._id, url) = spotify_module.create_playlist(self._oauth, self._name)
		if (self.exists(self._oauth, url) == False) :
			print("something bad happens here")

	def name(self) :
		return self._name

	def oauth(self) :
		return self._oauth

	def tracks(self) :
		return self._tracks

	def id(self) :
		return self._id

	def exists(self, oauth, url) :
		if url is None :
			return False
		return spotify_module.check_existence(oauth, url)

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	playlist = Playlist("Doldrums", OAUTH_token)
	print(playlist.name())
	print(playlist.id())
