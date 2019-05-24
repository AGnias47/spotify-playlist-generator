#!/usr/bin/python3
#
#   A. Gnias
#   date
#   CS 260
#   HW Assignment xxx
#
#   name and description
#
#   Linux tux5 4.15.0-43-generic
#   Python 3.6.7
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
