#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   spotify_module.py - Functions utilizing the Spotify API
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

import json
import requests
from sys import argv as arg
from sys import exit as sys_exit
from time import sleep


def get_artist_external_url(oauth, artist) :
	"""
	Returns the external_url for a specified artist
	Input: OAUTH token as a string, artist as a string
	Return Value: external_url as a string
	"""
	data = query_artist(oauth, artist)
	return data["external_urls"]["spotify"]
	
def get_artist_id(oauth, artist) :
	"""
	Returns the id for a specified artist
	Input: OAUTH token as a string, artist as a string
	Return Value: id as a string
	"""
	data = query_artist(oauth, artist)
	return data["id"]

def query_artist(oauth, artist) :
	"""
	Returns Spotify data of an artist in json format
	Input: OAUTH token as a string, artist as a string
	Return Value: Artist data as a dict
	"""
	SearchBase = "https://api.spotify.com/v1/search"
	SearchKey = "?q={0}&type=artist&market=US&limit=1".format(artist)
	SearchURL = SearchBase + SearchKey
	data = get_json_response_dict(oauth, SearchURL)
	d2 = data["artists"]["items"][0]
	return d2

def get_json_response_dict(oauth, SearchURL) :
	"""
	Returns a json dict from a REST get request
	Input: OAuth token and Search URL
	Return Value: Json returned from request as a dict
	"""
	headers = {'Content-Type': 'application/json',
              'Authorization': 'Bearer {0}'.format(oauth)}
	response = requests.get(SearchURL, headers=headers)
	if response.status_code != 200 :
		print("catch errors here")
		return "Something bad here"
	return json.loads(response.content.decode("utf-8"))

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
	data = get_json_response_dict(oauth, SearchURL)
	album_list = data["items"]
	data_list = list()
	for album in album_list :
		data_list.append(album[data_specifier])
	return data_list

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
	data = get_json_response_dict(oauth, SearchURL)
	track_list = data["items"]
	data_list = list()
	for track in track_list :
		data_list.append(track[data_specifier])
	return data_list

def print_pretty_json(jsonDataLoads) :
	"""
	Prints a formatted json to stdout
	Input: json formatted as a dict by Python JSON library
	Return Value: None (prints to stdout)
	"""
	print(json.dumps(jsonDataLoads, indent=3, sort_keys=False))

def create_playlist(oauth, name, description="Playlist generated from Spotify API") :
	"""
	Creates a playlist for the logged-in user
	Input: OAuth Token, Playlist name, Playlist description
	Output: True if playlist was created, else False
	"""
	PlaylistURL = "https://api.spotify.com/v1/me/playlists" 
	data = "{\"name\":\"" + name + "\",\"description\":\"" + description + "\",\"public\":false}" 
	headers = {'Accept': 'application/json',
              'Content-Type': 'application/json',
              'Authorization': 'Bearer {0}'.format(oauth)}
	response = requests.post(PlaylistURL, headers=headers, data=data)
	if response.status_code != 201 : 
		print(response.reason)
		return False
	return True
	
if __name__ == "__main__" :
	#Used for quick testing area
	#
	#Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	create_playlist(OAUTH_token, "testname")
