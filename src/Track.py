#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

class Track :
	def __init__(self, song, artist) :
		self._artist = artist
		self._song = song

	def artist(self) :
		return self._artist

	def song(self) :
		return self._song

	def setArtist(self, artist) :
		self._artist = artist

	def setSong(self, song) :
		self._song = song	


if __name__ == "__main__" :
	print("Nothing to run. Import class to use")
