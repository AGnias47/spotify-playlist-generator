#!/usr/bin/python3
#
#   A. Gnias
#   Created: 5/22/2019
#
#   parse_file_into_tracks.py - Parses a file containing a list
#   of delimited tracks into a list of Track objects
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0


from sys import path

path.append("../")
from src.Track import Track


def parse_playlist(fname, delimiter=","):
    """
    Generates a list of Tracks from a list delimited as [artist, song]

    Parameters
    ----------
    fname: str
        file name to parse into list
    delimiter: str (default is ",")
        string which splits artist and song name

    Returns
    -------
    list of Tracks

    """
    el = list()
    with open(fname, "r") as f:
        for line in f:
            contents = line.strip().split(delimiter)
            el.append(Track(contents[1].strip(), contents[0].strip()))
    return el
