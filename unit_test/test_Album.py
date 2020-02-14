#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import unittest
from sys import path

path.append("../")
from src.Album import Album


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.newAlbum = Album("Good Kid, M.A.A.D City", "Kendrick Lamar", 2012)
        self.blankAlbum = Album("Good Kid, M.A.A.D City")

    def test_name(self):
        self.assertEqual(self.newAlbum.name, "Good Kid, M.A.A.D City")

    def test_artist(self):
        self.assertEqual(self.newAlbum.artist, "Kendrick Lamar")

    def test_year(self):
        self.assertEqual(self.newAlbum.year, 2012)

    def test_tracks(self):
        self.assertEqual(self.newAlbum.tracks, None)

    def test_id(self):
        self.assertEqual(self.newAlbum.id, None)

    def test_set_artist(self):
        self.blankAlbum.artist = "Kendrick Lamar"
        self.assertEqual(self.blankAlbum.artist, "Kendrick Lamar")

    def test_set_year(self):
        self.blankAlbum.year = 2012
        self.assertEqual(self.blankAlbum.year, 2012)


if __name__ == "__main__":
    unittest.main()
