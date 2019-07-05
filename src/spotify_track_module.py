#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   spotify_track_module.py - Functions utilizing the Spotify API for
#                             interacting with tracks available through 
#                             Spotify
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
from general_functions import get_json_response_dict


#Define a global variable for the market being queried by country code
MARKET = "US"

def query_track(oauth, Track) :
	SearchBase = "https://api.spotify.com/v1/search"
	SearchKey = "?q={0}&type=track&market={1}&limit=10".format("EARFQUAKE", MARKET)
	return get_json_response_dict(oauth, SearchBase + SearchKey)#["artists"]["items"][0]



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
		return (None, None)
	data = json.loads(response.content.decode("utf-8"))
	return (data["id"], data["href"])


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	print_pretty_json(query_track(OAUTH_token, ""))
	
