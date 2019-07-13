#!/usr/bin/python3
#
#   A. Gnias
#
#   playlist_generator.py - Adds a CSV of tracks to a Spotify playlist
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("./src")
from src.track_parsing import *
from src.Playlist import Playlist
from src.Track import Track
from sys import argv as arg
from sys import exit as sys_exit


# Check if the OAUTH_token was provided as an argument
try :
	OAUTH_token= arg[1]
except :
	sys_exit("OAUTH token must be provided as an argument")

# Parse the tracks from the CSV
for track in parse_csv_playlist("test/Test_Artifacts/playlist.csv") :
	track.view_top_results(OAUTH_token)
