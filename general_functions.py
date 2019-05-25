#!/usr/bin/python3
#
#   A. Gnias
#
#   general_functions.py - General functions needed that do not utilize the Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.6.8
#   Vim 8.0 [tabstop=3]

def parse_csv_playlist(fname) :
	"""
	Generates a list containing items of the form [artist, song]
	Input: text file name in cwd
	Output: populated list
	"""
	el = list()
	with open(fname,'r') as f :
		for line in f :
			contents = line.strip().split(',')
			artist = contents[0].strip()
			song = contents[1].strip()
			el.append([artist, song])
	f.close()
	return el

print(parse_csv_playlist("playlist.csv"))
