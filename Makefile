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

utest_Playlist : test/test_Playlist.py
	cd test && $(PYTHON) test_Playlist.py

utest_Track : test/test_Track.py
	cd test && $(PYTHON) test_Track.py

utest : utest_Playlist utest_Track

ftest : test/test_spotify_modules.py
	cd test && $(PYTHON) test_spotify_modules.py $$(cat ../OAuth_Token)

test : utest ftest

run : playlist_generator.py
	$(PYTHON) playlist_generator.py $$(cat OAuth_Token)

