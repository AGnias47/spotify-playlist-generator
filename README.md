# SpotifyAPI Playlist Generator

## Description
This project allows a user to create a playlist in the Spotify library from a csv file of the form
```
Artist, Song
```
This is done by utilizing the Spotify API detailed [on the Spotify developer
website](https://developer.spotify.com/documentation/web-api/).

## Source Code
Link: https://github.com/AGnias47/SpotifyAPI

### Playlist Generation
A playlist can be generated via the following steps:
 1. As the project is not currently publicly distributed, each user must register an application separately
 via Spotify to retrieve their own ```client_id```, ```redirect_uri``` and ```client_secret```. This can be
 done by going to the [Spotify Developer's Dashboard](https://developer.spotify.com/dashboard/applications) 
 and clicking the button to ```Create a Client ID```
 2. Using these values, retrieve an OAuth Token by following the steps listed in the [Spotify web-api-auth-examples GitHub
repo](https://github.com/spotify/web-api-auth-examples). The OAuth token must have the following scopes defined (example
in line of Javascript): <br/>
```var scope = 'user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public';```
 3. Store the OAuth token in a file named ```OAuth_Token```
 4. Run the following command
```
./playlist_generator.py -f <Path to csv> -n <Playlist name> -d <Playlist description (Optional)>
```

### Internal Classes
The playlist generator utilizes the Playlist and Track classes, as well as a csv parser defined in the parse_file_into_tracks 
module, and a function in the general_functions module get_json_response_dict for general parsing of the API 
responses. The Album and Artist classes are mainly for demonstration purposes, but may be used in a 
future project.

### External Classes
The requests module is used for handling all REST API calls, and the fuzzywuzzy module is used for fuzzy matching when
searching for tracks through Spotify.

## Potential improvements
 * Calculate coverage
 * Remove unnecessary code and classes
 * User testing with more diverse array of songs
 * Full coverage of classes with available API calls
 * Allow for usage of already created playlists
 * GUI wrapper
 * Update instructions
    * Initially add client and secret
    * manually add access and refresh
    * Automate with refresh.py script
