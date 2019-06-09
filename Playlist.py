#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

class Playlist :
	def __init__(self, name, tracks=None, id=None) :
		self._name = name
		self._id = id
		self._tracks = tracks

	def name(self) :
		return self._name

	def id(self) :
		return self._id

	def tracks(self) :
		return self._tracks

	def create(self) :
		if self.exists() == False :
			#create the playlist here
			pass

	def exists(self) :
		if _id is None :
			return False
		#check through spofity API

if __name__ == "__main__" :
	playlist = Playlist("Doldrums")
	print(playlist.name())
	print(playlist.id())
