#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
from general_functions import get_json_response_dict, print_pretty_json


# Define a global variable for the market being queried by country code
MARKET = "US"
# Define a global variable for the limit of track search results to return
limit = 10

class Track :
	def __init__(self, song, artist, href=None, external_url=None, ID=None) :
		self._artist = artist
		self._song = song
		self._href = href
		self._external_url = external_url
		self._id = ID

	def artist(self) :
		return self._artist

	def song(self) :
		return self._song

	def href(self) :
		return self._href

	def external_url(self) :
		return self._external_url

	def id(self) :
		return self._id

	def set_artist(self, artist) :
		self._artist = artist

	def set_song(self, song) :
		self._song = song	

	def set_href(self, href) :
		self._href = href

	def set_external_url(self, external_url) :
		self._external_url = external_url

	def set_id(self, ID) :
		self._id = ID

	def spotify_query(self, oauth) :
		SearchBase = "https://api.spotify.com/v1/search"
		SearchKey = "?q={0}&type=track&market={1}&limit={2}".format(self._song, MARKET, limit)
		SearchItems = get_json_response_dict(oauth, SearchBase + SearchKey)["tracks"]["items"]
		for item in SearchItems :
			artist = item["artists"][0]["name"]
			if artist == self._artist : #make more tolerant, ex case insensitive, spelling
				self._href = item["href"]
				self._external_url = item["external_urls"]["spotify"]
				self._id = item["id"]
				return True
		return False

	def view_top_results(self, oauth) :
		SearchBase = "https://api.spotify.com/v1/search"
		SearchKey = "?q={0}&type=track&market={1}&limit={2}".format(self._song, MARKET, limit)
		SearchItems = get_json_response_dict(oauth, SearchBase + SearchKey)["tracks"]["items"]
		result = 1
		for item in SearchItems :
			artist = item["artists"][0]["name"]
			song = item["name"]
			album = item["album"]["name"]
			print("{0}. {1}".format(result, song))
			print("   " + artist)
			print("   " + album + '\n')
			result += 1
			#print_pretty_json(item)

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	EARFQUAKE = Track("EARFQUAKE", "Tyler, The Creator")
	EARFQUAKE.view_top_results(OAUTH_token)
