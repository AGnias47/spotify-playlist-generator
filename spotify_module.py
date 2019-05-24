#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

import json
import requests
from sys import argv as arg


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
	SearchURL = "https://api.spotify.com/v1/search"
	SearchKey="?q={0}&type=artist&market=US&limit=1".format(artist)
	headers = {'Content-Type': 'application/json',
              'Authorization': 'Bearer {0}'.format(oauth)}
	response = requests.get(SearchURL + SearchKey, headers=headers)
	if response.status_code != 200:
		print("An error occurred here")
	data = json.loads(response.content.decode('utf-8'))
	d2 = data["artists"]["items"][0]
	print(type(d2))
	return d2

def print_pretty_json(jsonDataLoads) :
	"""
	Prints a formatted json to stdout
	Input: json formatted as a dict by Python JSON library
	Return Value: None (prints to stdout)
	"""
	print(type(jsonDataLoads))
	print(json.dumps(jsonDataLoads, indent=3, sort_keys=False))

if __name__ == "__main__" :
	OAUTH_token= arg[1]
	artist = "Seal"
	print_pretty_json(query_artist(OAUTH_token, artist))
	print(get_artist_external_url(OAUTH_token, artist))
	print(get_artist_id(OAUTH_token, artist))
