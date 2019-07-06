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
from src.general_functions import *
from src.spotify_track_module import *
from src.spotify_playlist_module import add_track_to_playlist
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
playlist_tracks = parse_csv_playlist("test/Test_Artifacts/playlist.csv")

# Initialize the Playlist to be created
playlist = Playlist("SpotifyAPI Test Playlist", playlist_tracks)
if not playlist.spotify_init(OAUTH_token) :
	sys_exit("Playlist could not be created; exiting")

# Add any tracks unable to be added to this list
missed_tracks = list()
for track in playlist_tracks :
	print("Adding " + track.song() + " : " + track.artist() + " to " + playlist.name())
	if query_track(OAUTH_token, track) : # If track was found via search
		if add_track_to_playlist(OAUTH_token, playlist.id(), track.id()) : # add to playlist
			print("Success")
		else :
			missed_tracks.append(track.song() + ", " + track.artist())
	else :
		missed_tracks.append(track.song() + ", " + track.artist())

print("\nTracks unable to be found: ")
print(*missed_tracks, sep="\n")
