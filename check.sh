#!/bin/bash
# remove old .pyc clutter
find congredi/ -type f -name "*.pyc" -delete -print
# not executable
chmod -x -R congredi/
# Corrective regexes
    # use tabs
    find congredi/ -type f -exec sed -i "s/    /\t/g" {} \;
    # comma space
    find congredi/ -type f -exec sed -i "s/,/, /g; s/,\s\+/, /g" {} \;
    # trailing spaces
    find congredi/ -type f -exec sed -i "s/\s*$//g" {} \;
    # duplicate lines
    #'/./,/^$/!d'
    # comments with spaces
    #-i -e 's/ #\([^ ]\)/ # \1/g'
pylint congredi
nose2 congredi
