#!/bin/sh
while read line; do
	find . -name "$line" -prune -print -exec rm -rv {} \;
done < .gitignore;
chmod -x congredi/ -R 

pip install -q autopep8 nose2 setuptools-lint pylint

autopep8 -rvi congredi
pylint congredi
nose2 congredi

find congredi/ -type f -name "*.pyc" -delete -print
#mkdocs gh-deploy || echo "Docs failing..."

pip install -q -r requirements.txt

python setup.py build test bdist_wheel install 1>/dev/null
python setup.py lint || echo "Lint failed..."