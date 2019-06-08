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

from spotify_module import *
from filecmp import cmp
from sys import argv

def get_artist_JSON_test(OAUTH_token, artist) :
	print("Artist JSON data")
	print_pretty_json(query_artist(OAUTH_token, artist))
	sleep(test_delay)

def get_artist_data_test(OAUTH_token, artist) :
	print("Specific artist data")
	external_url = get_artist_external_url(OAUTH_token, artist)
	SealID = get_artist_id(OAUTH_token, artist)
	print("{}'s external URL: {}".format(artist, external_url))
	print("{}'s ID: {}".format(artist, SealID))
	print("{}'s external URL: {}".format(artist, external_url), file=open("Test_Artifacts/artist_data_test", "w"))
	print("{}'s ID: {}".format(artist, SealID), file=open("Test_Artifacts/artist_data_test", "a"))
	sleep(test_delay)

def get_album_data_test(OAUTH_token, artist, SealID) :
	print("Album Data Functions")
	print(get_album_data_by_artist(OAUTH_token, SealID))
	print(get_album_data_by_artist(OAUTH_token, SealID, "href"))
	print(get_album_data_by_artist(OAUTH_token, SealID, "id"))
	print(get_album_data_by_artist(OAUTH_token, SealID), file=open("Test_Artifacts/album_data_test", "w"))
	print(get_album_data_by_artist(OAUTH_token, SealID, "href"), file=open("Test_Artifacts/album_data_test", "a"))
	print(get_album_data_by_artist(OAUTH_token, SealID, "id"), file=open("Test_Artifacts/album_data_test", "a"))
	sleep(test_delay)

def get_track_data_test(OAUTH_token, artist) :
	print("Track Data Functions")
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi"))
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi", "href"))
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi", "id"))
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi"), file=open("Test_Artifacts/track_data_test", "w"))
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi", "href"), file=open("Test_Artifacts/track_data_test", "a"))
	print(get_tracks_by_album_id(OAUTH_token, "2Fd1KIL5aUNTl40H3OkOQi", "id"), file=open("Test_Artifacts/track_data_test", "a"))

if __name__ == "__main__" :
	#Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	#Artist to use as an example
	artist = "Seal"
	SealID = get_artist_id(OAUTH_token, artist)
	test_delay = 3
	
	get_artist_JSON_test(OAUTH_token, artist)
	get_artist_data_test(OAUTH_token, artist) 
	assert cmp("Test_Artifacts/expected_artist_data_test", "Test_Artifacts/artist_data_test")
	get_album_data_test(OAUTH_token, artist, SealID)
	assert cmp("Test_Artifacts/expected_album_data_test", "Test_Artifacts/album_data_test")
	get_track_data_test(OAUTH_token, artist)
	assert cmp("Test_Artifacts/expected_track_data_test", "Test_Artifacts/track_data_test")
