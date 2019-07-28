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
from sys import argv as arg
from sys import exit as sys_exit
from src.general_functions import get_json_response_dict

class Album :

	def __init__(self, name, artist = None, year = None, tracks = None, ID = None) :
		self._name = name
		self._artist = artist
		self._year = year
		self._tracks = tracks
		self._id = ID

	def get_name(self) :
		return self._name

	def get_artist(self) :
		return self._artist

	def get_year(self) :
		return self._year

	def get_tracks(self) :
		return self._tracks

	def get_id(self) :
		return self._id

	def set_artist(self, artist) :
		self._artist = artist

	def set_year(self, year) :
		self._year = year

	def set_album_metadata(self, oauth) :
		#Search for an album here and set all properties; if 
		#artist or year are defined, use in search, else find and set
		self._tracks = get_tracks_by_album_id(self, oauth)

	def get_tracks_by_album_id(self, oauth) :
		"""
		Get data on an album's tracks. Can return data as a list of 
		either the names of an album's tracks as a string, the URL
		used to access the tracks, or the ID of the tracks.
		Input: OAuth Token, album ID, data specifier (can be either
		name, href, or id; takes name by default)
		Return value: list of specified data as strings
		"""
		SearchURL = "https://api.spotify.com/v1/albums/{}/tracks".format(self._id)
		return [track[name] for track in get_json_response_dict(oauth,SearchURL)["items"]]

