#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   spotify_album_module.py - Functions utilizing the Spotify API for
#                             interacting with an artist's albums
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from sys import argv as arg
from sys import exit as sys_exit
from src.general_functions import get_json_response_dict


def get_album_data_by_artist(oauth, artist_id, data_specifier="name") :
	"""
	Get data on an artists albums. Can return data as a list of 
	either the names of an artist's albums as a string, the URL
	used to access the albums, or the ID of the albums.
	Input: OAuth Token, artist ID, data specifier (can be either
	name, href, or id; takes name by default)
	Return value: list of specified data as strings
	"""
	SearchURL = "https://api.spotify.com/v1/artists/{}/albums?include_groups=album,single&country=US&limit=50".format(artist_id)
	return [album[data_specifier] for album in get_json_response_dict(oauth, SearchURL)["items"]]


def get_tracks_by_album_id(oauth, album_id, data_specifier="name") :
	"""
	Get data on an album's tracks. Can return data as a list of 
	either the names of an album's tracks as a string, the URL
	used to access the tracks, or the ID of the tracks.
	Input: OAuth Token, album ID, data specifier (can be either
	name, href, or id; takes name by default)
	Return value: list of specified data as strings
	"""
	SearchURL = "https://api.spotify.com/v1/albums/{}/tracks".format(album_id)
	return [track[data_specifier] for track in get_json_response_dict(oauth,SearchURL)["items"]]


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
