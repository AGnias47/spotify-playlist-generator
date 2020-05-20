#
#   A. Gnias
#
#   Makefile - Used for SpotifyAPI Repository
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Make 4.2.1
#   Vim 8.0

PYTHON = python3
VIEWER = less
README_VIEWER = mdless
SHELL = bash

.PHONY : clean view readme license runnode apidocs \
utest_Playlist utest_Track test utest_Artist utest_Album utest \
ftest_Playlist ftest_Track ftest_general test_parameterinput ftest \
test run

clean :
	git clean -dxf -e keys.json -e .idea/

view : playlist_generator.py
	$(VIEWER) playlist_generator.py

readme : README.md
	${README_VIEWER} README.md

license : LICENSE
	$(VIEWER) LICENSE

runnode : 
	node ~/spotify_auth_page/app.js

apidocs :
	cd sphinx && sphinx-apidoc -f -o source/ ../.

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

test_parameterinput : playlist_generator.py
	$(PYTHON) playlist_generator.py

utest : utest_Playlist utest_Track utest_Artist utest_Album

ftest : ftest_Playlist ftest_Track ftest_general

test : utest ftest

run : playlist_generator.py
	$(PYTHON) playlist_generator.py -k keys.json -f playlist.csv -n Spotify_API_$$(date +%m_%d_%Y) -d "Playlist from the spotify API"


