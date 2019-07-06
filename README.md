# SpotifyAPI
Development projects utilizing the Spotify API detailed at https://developer.spotify.com/documentation/web-api/

## Playlist Generator (playlist_generator.py)
Creates a playlist from a csv of the form:
```
Song, Artist
```

## OAuth Token retrieval
Currently just getting this by running the steps listed at https://github.com/spotify/web-api-auth-examples.

There is probably an easier way to do this. Look into method used in spotipy module.

## Planned improvements
App is still in the early stages of development. Planned improvements include:
 * Script for easily viewing top result of search function
 * Dash separated list as opposed to CSV
 * More tolerance for comparing found song against artist
 * Accounting for songs with special characters
 * Tolerance for song from an artist containing features
 * Easier method of obtaining OAuth Token
 * Validate the OAuth Token works before running
 * User testing with more diverse array of songs
 * Allow user to pass in custom CSV, Playlist name, etc.
 * 100% coverage of functional testing
 * GUI wrapper (stretch goal)
