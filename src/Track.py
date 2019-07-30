#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   Track.py - Class for interacting with Tracks through
#   the Spotify API.
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.general_functions import get_json_response_dict, print_pretty_json
from fuzzywuzzy import fuzz as fuzzy


# Define a global variable for the market being queried by country code
MARKET = "US"
# Define a global variable for the limit of track search results to return
limit = 10


class Track :
	def __init__(self, song, artist, href=None, external_url=None, ID=None) :
		self.artist = artist
		self.song = song
		self.href = href
		self.external_url = external_url
		self.ID = ID

	def spotify_query(self, oauth, lev_partial_ratio=75) :
		SearchBase = "https://api.spotify.com/v1/search"
		SearchKey = "?q={0}&type=track&market={1}&limit={2}".format(self.song, MARKET, limit)
		SearchItems = get_json_response_dict(oauth, SearchBase + SearchKey)["tracks"]["items"]
		for item in SearchItems :
			artist = item["artists"][0]["name"]
			song = item["name"]
			if fuzzy.partial_ratio(artist.lower(), self.artist.lower()) > lev_partial_ratio and \
				fuzzy.partial_ratio(song.lower(), self.song.lower()) > lev_partial_ratio :
				self.href = item["href"]
				self.external_url = item["external_urls"]["spotify"]
				self.ID = item["id"]
				return True
		return False

	def view_top_results(self, oauth) :
		SearchBase = "https://api.spotify.com/v1/search"
		SearchKey = "?q={0}&type=track&market={1}&limit={2}".format(self.song, MARKET, limit)
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
