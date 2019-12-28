# SpotifyAPI
Development projects utilizing the Spotify API detailed at https://developer.spotify.com/documentation/web-api/

## Playlist Generator (playlist_generator.py)
Creates a playlist from a csv of the form:
```
Song, Artist
```

Can be run with the following command:
```
./playlist_generator.py -t <API Token> -f <Path to csv> -n <Playlist name> -d <Playlist description (Optional)>
```


## OAuth Token retrieval
Currently just getting this by running the steps listed at https://github.com/spotify/web-api-auth-examples.

There is probably an easier way to do this. Look into method used in spotipy module.
## Continued work
 * Docstring cleanup
 * Easier method of using / obtaining OAuth Token
## Potential improvements
 * User testing with more diverse array of songs
 * Full coverage of classes with available API calls
 * Allow for usage of already created playlists
 * GUI wrapper
