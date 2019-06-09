#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

class Playlist :
	def __init__(self, name, id=None) :
		self._name = name
		self._id = id

	def name(self) :
		return self._name

	def id(self) :
		return self._id

	#def create(self) :
		#stub

	#def exists(self, name) :
		#stub

if __name__ == "__main__" :
	playlist = Playlist("Doldrums")
	print(playlist.name())
	print(playlist.id())
