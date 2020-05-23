#!/usr/bin/python3
#
#   A. Gnias
#   Created: 2/15/2020
#
#   Linux 5.3.0-29-generic #31-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Defines specific exceptions to throw
"""


class PlaylistNotInitializedError(Exception):
    """
    Exception to raise if a playlist cannot be created in Spotify
    """

    def __init__(self, msg=None):
        super().__init__(msg)


class UnsuccessfulGetRequest(Exception):
    """
    Exception to raise if a GET request to the API fails
    """

    def __init__(self, msg=None):
        super().__init__(msg)
