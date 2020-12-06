#!/usr/bin/python3
#
#   A. Gnias
#   Created: 5/22/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Parses a file containing a list of delimited tracks into a list of Track objects
"""

from src.Track import Track


def parse_file_playlist(fname, delimiter=","):
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
            el.append(_get_list_of_tracks(line, delimiter))
    return el


def parse_string_playlist(content, delimiter=","):
    """
    Generates a list of Tracks from a block of text delimited as [artist, song]\n

    Parameters
    ----------
    content: str
        Text containing tracks separated by new lines
    delimiter: str (default is ",")
        string which splits artist and song name

    Returns
    -------
    list of Tracks

    """
    el = list()
    for line in content.split("\n"):
        line.strip()
        if len(line) > 0:
            el.append(_get_list_of_tracks(line, delimiter))
    return el


def _get_list_of_tracks(line, delimiter):
    """
    Helper function for generating track lists from files and string blocks. Parses an individual track string into
    a Track object

    Parameters
    ----------
    line: str
        Contains artist and track separated by a delimiter
    delimiter: str
        Character(s) separating artist and track

    Returns
    -------
    Track
    """
    contents = line.strip().split(delimiter)
    try:
        return Track(contents[1].strip(), contents[0].strip())
    except IndexError:
        return Track(contents[0].strip(), contents[0].strip())
