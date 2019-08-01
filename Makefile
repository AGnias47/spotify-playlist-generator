#
#   A. Gnias
#
#   Makefile - Used for SpotifyAPI Repository
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Make 4.2.1
#   Vim 8.0 [tabstop=3]

PYTHON = python3
VIEWER = less
SHELL = bash

.PHONY : clean view license test run

clean :
	rm -rf *.pyc __pycache__

view : playlist_generator.py
	$(VIEWER) playlist_generator.py

license : LICENSE
	$(VIEWER) LICENSE

runnode : 
	node ~/spotifyapitestbed/web-api-auth-examples/authorization_code/app.js

utest_Playlist : unit_test/test_Playlist.py
	cd unit_test && $(PYTHON) test_Playlist.py

utest_Track : unit_test/test_Track.py
	cd unit_test && $(PYTHON) test_Track.py

utest_Artist : unit_test/test_Artist.py
	cd unit_test && $(PYTHON) test_Artist.py

utest_Album : unit_test/test_Album.py
	cd unit_test && $(PYTHON) test_Album.py

ftest_Playlist : functional_test/ftest_Playlist.py
	cd functional_test && $(PYTHON) ftest_Playlist.py

ftest_Track : functional_test/ftest_Track.py
	cd functional_test && $(PYTHON) ftest_Track.py

ftest_general : functional_test/ftest_general_functions.py
	cd functional_test && $(PYTHON) ftest_general_functions.py

utest : utest_Playlist utest_Track utest_Artist utest_Album

ftest : ftest_Playlist ftest_Track ftest_general

test : utest ftest

run : playlist_generator.py
	$(PYTHON) playlist_generator.py -t $$(cat OAuth_Token) -f functional_test/Test_Artifacts/playlist.csv -n Spotify_API_$$(date +%m_%d_%Y) -d "Playlist from the spotify API"

test_parameterinput : playlist_generator.py
	$(PYTHON) playlist_generator.py
