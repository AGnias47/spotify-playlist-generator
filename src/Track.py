#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]


class Track :
	def __init__(self, song, artist, href=None, external_url=None) :
		self._artist = artist
		self._song = song
		self._href = href
		self._external_url = external_url

	def artist(self) :
		return self._artist

	def song(self) :
		return self._song

	def href(self) :
		return self._href

	def external_url(self) :
		return self._external_url

	def set_artist(self, artist) :
		self._artist = artist

	def set_song(self, song) :
		self._song = song	

	def set_href(self, href) :
		self._href = href

	def set_external_url(self, external_url) :
		self._external_url = external_url

	def set_track_data(self, oauth) :
		(self._href, self._external_url) = query_track(oauth, self)

if __name__ == "__main__" :
	print("Nothing to run. Import class to use")
