#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

from general_functions import *
from Playlist import Playlist

playlistTracks = parse_csv_playlist("playlist.csv")
playlist = Playlist("Test Playlist", playlistTracks)
#create an empty playlist in spotify or append to an existing one
#add the song to the created playlist
