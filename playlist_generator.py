#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("./src")
from src.general_functions import *
from src.Playlist import Playlist
from sys import argv as arg
from sys import exit as sys_exit

try :
	OAUTH_token= arg[1]
except :
	sys_exit("OAUTH token must be provided as an argument")
playlist_tracks = parse_csv_playlist("test/Test_Artifacts/playlist.csv") #method for parsing dash separated values
playlist = Playlist("SpotifyAPI Test Playlist", playlist_tracks)
#if not playlist.spotifyInit(OAUTH_token) :
#	sys_exit("Playlist could not be created; exiting")
for track in playlist_tracks :
	print("Adding " + track.song() + " : " + track.artist() + " to " + playlist.name())
	if query_track(OAUTH_token, track) :
		#add to playlist
	else :
		#could not add to playlist
