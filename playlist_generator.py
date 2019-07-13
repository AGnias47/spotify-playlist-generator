#!/usr/bin/python3
#
#   A. Gnias
#
#   playlist_generator.py - Adds a CSV of tracks to a Spotify playlist
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from src.track_parsing import *
from src.Playlist import Playlist
from src.Track import Track
from sys import argv as arg
from sys import exit as sys_exit
from os import path
import getopt

def process_commandline_parameters() :
	"""
	Processes commandline parameters
	Input: None (hard-coded with the function)
	Output: 
	"""
	try :
		options, arguments = getopt.getopt(arg[1:], "t:p:n:", ["token=", "playlist=", "name="])
	except getopt.GetoptError as err:
		print(err)
		sys_exit(1)
	for o, a in options :
		if o in ("-t", "--token") :
			OAuth_Token = a
		elif o in ("-p", "--playlist") : 
			Playlist_Name = a
		else :
			print("Unhandled option; ignoring {1}", o)
	try : OAuth_Token
	except :
		if path.exists("OAuth_Token") :
			with open("OAuth_Token") as T :
				OAuth_Token = T.read().strip()
			T.closed
		else :
			OAuth_Token = input("Sender's email: ").strip()
	try : Playlist_Name
	except :
		Playlist_Name = input("File containing tracks to add to playlist: (playlist.csv) ").strip()
		if Playlist_Name == "" :
			Playlist_Name = "playlist.csv"
	return (OAuth_Token, Playlist_Name)

def main() :
	(OAuth_Token, Playlist_Name) = process_commandline_parameters()

	# Parse the tracks from the CSV
	playlist_tracks = parse_csv_playlist(Playlist_Name)

	# Initialize the Playlist to be created
	playlist = Playlist("SpotifyAPI Test Playlist", playlist_tracks)
	if not playlist.spotify_init(OAuth_token) :
		sys_exit("Playlist could not be created; exiting")

	# Add any tracks unable to be added to this list
	missed_tracks = list()
	for track in playlist_tracks :
		print("Adding " + track.song() + " : " + track.artist() + " to " + playlist.name())
		if track.spotify_query(OAuth_token) : # If track was found via search
			if playlist.spotify_add_track(OAuth_token, track.id()) : # add to playlist
				print("Success")
			else :
				missed_tracks.append(track.song() + ", " + track.artist())
		else :
			missed_tracks.append(track.song() + ", " + track.artist())

	print("\nTracks unable to be found: ")
	print(*missed_tracks, sep="\n")
