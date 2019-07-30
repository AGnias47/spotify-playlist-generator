#!/usr/bin/python3
#
#   A. Gnias
#
#   playlist_generator.py - Adds a CSV of tracks to a Spotify playlist
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from src.general_functions import *
from src.parse_file_into_tracks import *
from src.Playlist import Playlist
from src.Track import Track
from sys import argv as arg, exit
from os import path
import getopt


def process_commandline_parameters() :
	"""
	Processes commandline parameters
	Input: None (hard-coded with the function)
	Output: 
	"""
	try :
		options, arguments = getopt.getopt(arg[1:], "t:f:n:d:", ["token=", "filename=", "name=", "description="])
	except getopt.GetoptError as err:
		print(err)
		exit(1)
	for o, a in options :
		if o in ("-t", "--token") :
			OAuth_Token = a
		elif o in ("-f", "--filename") : 
			Playlist_Filename = a
		elif o in ("-n", "--name") :
			Playlist_Name = a
		elif o in ("-d", "--description") :
			Description = a
		else :
			print("Unhandled option; ignoring {1}", o)
	try : OAuth_Token
	except :
		if path.exists("OAuth_Token") :
			with open("OAuth_Token") as T :
				OAuth_Token = T.read().strip()
			T.closed
		else :
			OAuth_Token = input("OAuth Token: ").strip()
	try : Playlist_Filename
	except :
		Playlist_Filename = input("File containing tracks to add to playlist: (playlist.csv) ").strip()
		if Playlist_Filename == "" :
			Playlist_Filename = "playlist.csv"
	try : Playlist_Name
	except : 
		Playlist_Name = input("Playlist name: (SpotifyAPI Test Playlist) ").strip()
		if Playlist_Name == "" :
			Playlist_Name = "SpotifyAPI Test Playlist"
	try : Description
	except :
		Description = "Playlist generated from playlist_generator.py"
	return (OAuth_Token, Playlist_Filename, Playlist_Name, Description)


def main() :
	(OAuth_Token, Playlist_Filename, Playlist_Name, Description) = process_commandline_parameters()

	if not path.exists(Playlist_Filename) :
		exit("Could not find " + Playlist_Filename + "; exiting")

	# Parse the tracks from the CSV
	playlist_tracks = parse_playlist(Playlist_Filename)

	# Initialize the Playlist to be created
	playlist = Playlist(Playlist_Name, playlist_tracks)
	if not playlist.spotify_init(OAuth_Token, Description) :
		exit("Playlist could not be created; exiting")

	# Add any tracks unable to be added to this list
	missed_tracks = list()
	for track in playlist_tracks :
		print("Adding " + track.song + " : " + track.artist + " to " + playlist.name)
		if track.spotify_query(OAuth_Token) : # If track was found via search
			if playlist.spotify_add_track(OAuth_Token, track.ID) : # add to playlist
				print("Success")
			else :
				missed_tracks.append(track.song + ", " + track.artist)
		else :
			missed_tracks.append(track.song + ", " + track.artist)

	print("\nTracks unable to be found: ")
	print(*missed_tracks, sep="\n")


main()
