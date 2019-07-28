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


class Artist :

	def __init__(self, name, oauth = None) :
		self._name = name
		if oauth is None :
			self._external_url = None
			self._id = None
		else :
			set_artist_external_url(oauth)
			set_artist_id(oauth)

	def get_name(self) :
		return self._name

	def get_external_url(self) :
		return self._external_url

	def get_id(self) :
		return self._id

	def query_artist(oauth, artist) :
		"""
		Returns Spotify data of an artist in json format
		Input: OAUTH token as a string, artist as a string
		Return Value: Artist data as a dict
		"""
		SearchBase = "https://api.spotify.com/v1/search"
		SearchKey = "?q={0}&type=artist&market=US&limit=1".format(artist)
		return get_json_response_dict(oauth, SearchBase + SearchKey)["artists"]["items"][0]

	def set_artist_external_url(self, oauth) :
		"""
		Returns the external_url for a specified artist
		Input: OAUTH token as a string, artist as a string
		Return Value: external_url as a string
		"""
		self._external_url = query_artist(oauth, self._name)["external_urls"]["spotify"]

	def set_artist_id(self, oauth) :
		"""
		Returns the id for a specified artist
		Input: OAUTH token as a string, artist as a string
		Return Value: id as a string
		"""
		_id = query_artist(oauth, self._name)["id"]

	def get_album_data_by_artist(self, oauth) :
		"""
		Get data on an artists albums. Can return data as a list of 
		either the names of an artist's albums as a string, the URL
		used to access the albums, or the ID of the albums.
		Input: OAuth Token, artist ID, data specifier (can be either
		name, href, or id; takes name by default)
		Return value: list of specified data as strings
		"""
		if self._id is None :
			set_artist_id(oauth)
		SearchURL = "https://api.spotify.com/v1/artists/{}/albums?include_groups=album,single&country=US&limit=50".format(self._id)
		return [album["name"] for album in get_json_response_dict(oauth, SearchURL)["items"]]
