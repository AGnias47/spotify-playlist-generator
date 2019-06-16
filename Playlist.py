#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

import spotify_module

class Playlist :
	def __init__(self, name, oauth=None, tracks=None, id=None) :
		self._name = name
		self._id = id
		self._tracks = tracks
		self._oauth = oauth
		if self._oauth is not None and id is None :
			spotify_module.create_playlist(self._oauth, self._name)

	def name(self) :
		return self._name

	def oauth(self) :
		return self._oauth

	def tracks(self) :
		return self._tracks

	def id(self) :
		return self._id

	def exists(self) :
		if _id is None :
			return False
		#check through spofity API

if __name__ == "__main__" :
	playlist = Playlist("Doldrums")
	print(playlist.name())
	print(playlist.id())
