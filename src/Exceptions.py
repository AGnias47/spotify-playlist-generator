#!/usr/bin/python3
#
#   A. Gnias
#   Created: 2/15/2020
#
#   Exceptions.py - defines specific exceptions to throw
#
#   Linux 5.3.0-29-generic #31-Ubuntu
#   Python 3.7.5
#   Vim 8.0


class PlaylistNotInitializedError(Exception):
    """
    Exception to raise if a playlist cannot be created in Spotify
    """

    pass
