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
from general_functions import get_json_response_dict, print_pretty_json
from Track import Track


# Define a global variable for the market being queried by country code
MARKET = "US"

def query_track(oauth, Track) :
	limit = 10
	SearchBase = "https://api.spotify.com/v1/search"
	SearchKey = "?q={0}&type=track&market={1}&limit={2}".format(Track.song(), MARKET, limit)
	SearchItems = get_json_response_dict(oauth, SearchBase + SearchKey)["tracks"]["items"]
	for item in SearchItems :
		artist = item["artists"][0]["name"]
		if artist == Track.artist() : #make more tolerant, ex case insensitive, spelling
			Track.set_href(item["href"])
			Track.set_external_url(item["external_urls"]["spotify"])
			Track.set_id(item["id"])
			return True
	return False


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	EARFQUAKE = Track("EARFQUAKE", "Tyler, The Creator")
	print(query_track(OAUTH_token, EARFQUAKE))
