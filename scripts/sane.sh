#!/bin/sh
# gosh I tried a lot of things... Here's an example...
#files=$(cat .gitignore | tr "\n" "\|"); find -regextype posix-extended -regex '.*($files)' -print
while read line; do
	find . -name "$line" -prune -print -exec rm -rv {} \;
#-delete
done < .gitignore;

exit
# remove old .pyc clutter
find congredi/ -type f -name "*.pyc" -delete -print
# not executable
chmod -x congredi/ -R 
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
