#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   spotify_artist_module.py - Functions utilizing the Spotify API for
#                       interacting with artist data
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
from general_functions import get_json_response_dict


def get_artist_external_url(oauth, artist) :
	"""
	Returns the external_url for a specified artist
	Input: OAUTH token as a string, artist as a string
	Return Value: external_url as a string
	"""
	return query_artist(oauth, artist)["external_urls"]["spotify"]


def get_artist_id(oauth, artist) :
	"""
	Returns the id for a specified artist
	Input: OAUTH token as a string, artist as a string
	Return Value: id as a string
	"""
	return query_artist(oauth, artist)["id"]


def query_artist(oauth, artist) :
	"""
	Returns Spotify data of an artist in json format
	Input: OAUTH token as a string, artist as a string
	Return Value: Artist data as a dict
	"""
	SearchBase = "https://api.spotify.com/v1/search"
	SearchKey = "?q={0}&type=artist&market=US&limit=1".format(artist)
	return get_json_response_dict(oauth, SearchBase + SearchKey)["artists"]["items"][0]


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
