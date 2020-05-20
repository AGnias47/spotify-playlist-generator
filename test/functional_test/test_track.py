#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import unittest

from src.Track import Track
from spotify_token_refresh.refresh import get_access_token


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.access_token = get_access_token()
        self.track = Track("Blue in Green", "Miles Davis")

    def test_query(self):
        self.assertTrue(self.track.spotify_query(self.access_token))
