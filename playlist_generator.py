#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

from general_functions import *

playlist = parse_csv_playlist("playlist.csv")
#create an empty playlist in spotify or append to an existing one
for song in playlist :
	artist = song[0]
	track = song[1]
	#add the song to the created playlist
