#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import unittest

from src.Playlist import Playlist
from spotify_token_refresh.refresh import get_access_token


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.access_token = get_access_token()
        self.playlist = Playlist("__TEST__")
        self.track_id = "1KueOLeUZpaNRK2InckxVT"

    def test_add_track(self):
        self.assertTrue(self.playlist.spotify_init(self.access_token))
        self.assertTrue(self.playlist.spotify_add_track(self.access_token, self.track_id))
        print("Remove __TEST__ Playlist from Spotify; no API call to do this manually as of 7/27/19\n")
