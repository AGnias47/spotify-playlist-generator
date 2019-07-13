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
 * Ensure all scripts can run from anywhere within repo (clean up relative imports)
 * Allow user to pass in custom CSV, Playlist name, etc.
 * More tolerance for comparing found song against artist
 * Dash separated list as opposed to CSV
 * 100% coverage of functional testing
 * Better sync with Playlist object and actual Spotify playlist
 * Allow for usage of already created playlists
 * Automated test for more varied testing of adding tracks
 * Accounting for songs with special characters
 * Tolerance for song from an artist containing features
 * Easier method of obtaining OAuth Token
 * Validate the OAuth Token works before running
 * User testing with more diverse array of songs
 * GUI wrapper (stretch goal)
