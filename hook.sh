# Install this check into your git hooks...
# ln -s -f ../../check.sh .git/hooks/pre-commit
#git stash --keep-index
#set +e
#trap 'git stash pop -q' EXIT
#git reset --hard --index
#git stash pop -q
# #!/bin/bash

# set +e
# bash -e <<TRY
#   cd /does/not/exist
# TRY
# if [ $? -ne 0 ]; then
#   echo caught exception
# fi
RESULT=$?
echo "finished"
[ $RESULT -ne 0 ] && echo "Commit aborted!" exit 1
exit 0
