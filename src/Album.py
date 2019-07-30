#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 7/27/2019
#
#   Artist.py - Class utilizing the Spotify API for
#               interacting with artist data. Performs
#               more complex functionality extending
#               beyond and unrelated to Track class.
# 
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.general_functions import get_json_response_dict


class Album :

	def __init__(self, name, artist=None, year=None, tracks=None, ID=None) :
		self.name = name
		self.artist = artist
		self.year = year
		self.tracks = tracks
		self.ID = ID

	def set_album_metadata(self, oauth) :
		# Search for an album here and set all properties; if
		# artist or year are defined, use in search, else find and set
		self.tracks = self.get_tracks_by_album_id(self, oauth)

	def get_tracks_by_album_id(self, oauth) :
		"""
		Get data on an album's tracks. Can return data as a list of 
		either the names of an album's tracks as a string, the URL
		used to access the tracks, or the ID of the tracks.
		Input: OAuth Token, album ID, data specifier (can be either
		name, href, or id; takes name by default)
		Return value: list of specified data as strings
		"""
		SearchURL = "https://api.spotify.com/v1/albums/{}/tracks".format(self.ID)
		return [track[self.name] for track in get_json_response_dict(oauth, SearchURL)["items"]]

