#!/usr/bin/python3
#
#   A. Gnias
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

import unittest

from spotifytools.track import Track
from spotifytools.token_refresh import get_access_token


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.access_token = get_access_token()
        self.track = Track("Blue in Green", "Miles Davis")

    def test_query(self):
        self.assertTrue(self.track.spotify_query(self.access_token))

    def test_view_top_results(self):
        self.assertEqual(self.track.view_top_results(self.access_token, limit=1), None)
