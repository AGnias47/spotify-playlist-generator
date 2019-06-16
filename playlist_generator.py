#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from general_functions import *
from Playlist import Playlist

try :
	OAUTH_token= arg[1]
except :
	sys_exit("OAUTH token must be provided as an argument")

playlistTracks = parse_csv_playlist("playlist.csv")
playlist = Playlist("Test Playlist", playlistTracks, OAUTH_token)
#add the song to the created playlist
