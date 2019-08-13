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

## Potential improvements
 * Easier method of obtaining OAuth Token
 * User testing with more diverse array of songs
 * Full coverage of classes with available API calls
 * Better sync with classes and actual Spotify objects
 * Allow for usage of already created playlists
 * GUI wrapper (stretch goal)
