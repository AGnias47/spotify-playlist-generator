#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   general_functions.py - Functions supporting use of the Spotify API
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
from Track import Track


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
			el.append(Track(contents[1].strip(), contents[0].strip()))
	f.close()
	return el


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
	print(parse_csv_playlist("Test_Artifacts/playlist.csv"))

