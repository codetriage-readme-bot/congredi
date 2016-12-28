#!/bin/sh
# Install this check into your git hooks...
# ln -s -f ../../check.sh .git/hooks/pre-commit
git stash --keep-index
set +e
#trap 'git stash pop -q' EXIT
while read line; do
	find . -name "$line" -prune -print -exec rm -r {} \;
done < .gitignore;
chmod -x congredi/ -R 
pip install -q autopep8 nose2 setuptools-lint pylint
autopep8 -rvi congredi 1>/dev/null
pylint congredi 1>/dev/null || echo "Lint failed..."
pip install -q -r requirements.txt
nose2 congredi 1>/dev/null
#mkdocs gh-deploy || echo "Docs failing..."
python setup.py build bdist_wheel 1>/dev/null
find congredi/ -type f -name "*.pyc" -delete
RESULT=$?
git stash pop -q
[ $RESULT -ne 0 ] && echo "Commit aborted!" exit 1
exit 0

# #!/bin/bash

# set +e
# bash -e <<TRY
#   cd /does/not/exist
# TRY
# if [ $? -ne 0 ]; then
#   echo caught exception
# fi