#!/bin/bash
#
#   A. Gnias
#
#   Kubuntu 5.16.5
#   Linux 5.3.0-40-generic #32-Ubuntu
#   GNU bash, version 5.0.3(1)-release

sphinx-apidoc -f -o source/ ../.

make html

cd build/html
mv _sources sources
mv _static static
find . -type f -exec sed -i 's/_sources/sources/g' {} \;
find . -type f -exec sed -i 's/_static/static/g' {} \;
cd ../..

rm -rf ../docs
mv build/html ../docs
