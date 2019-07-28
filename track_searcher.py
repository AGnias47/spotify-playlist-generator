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
from src.parse_file_into_tracks import *
from src.Track import Track
from sys import argv as arg, exit


# Check if the OAUTH_token was provided as an argument
if len(arg) > 1 :
	OAuth_Token = arg.pop()
else :
	try :
		with open("OAuth_Token", 'r') as F :
			OAuth_Token = F.read().strip()
		F.closed
	except :
		exit("OAuth Token not provided as an argument or at OAuth_Token. Exiting")


# Parse the tracks from the CSV
for track in parse_playlist("functional_test/Test_Artifacts/playlist.csv") :
	track.view_top_results(OAuth_Token)
