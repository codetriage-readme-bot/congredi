#!/bin/sh
git stash -q --keep-index
set +e
#trap 'git stash pop -q' EXIT
while read line; do
	find . -name "$line" -prune -print -exec rm -rv {} \;
done < .gitignore;
chmod -x congredi/ -R 
pip install -q autopep8 nose2 setuptools-lint pylint
autopep8 -rvi congredi
pylint congredi || echo "Lint failed..."
pip install -q -r requirements.txt
nose2 congredi
#mkdocs gh-deploy || echo "Docs failing..."
python setup.py build bdist_wheel 1>/dev/null
find congredi/ -type f -name "*.pyc" -delete -print
RESULT=$?
git stash pop -q
[ $RESULT -ne 0 ] && echo "Commit aborted!" exit 1
exit 0

# #!/bin/bash

# set +e
# bash -e <<TRY
#   echo hello
#   cd /does/not/exist
#   echo world
# TRY
# if [ $? -ne 0 ]; then
#   echo caught exception
# fi