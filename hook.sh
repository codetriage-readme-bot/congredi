#!/bin/bash
# Install this check into your git hooks...
# ln -s -f ../../check.sh .git/hooks/pre-commit
# git stash --keep-index
set +e
bash -e <<TRY
  ./scripts.sh
TRY
trap 'git stash pop -q' EXIT

if [ $? -ne 0 ]; then
  echo caught exception
fi
RESULT=$?
echo "finished"
# git reset --hard --index
# git stash pop -q
[ $RESULT -ne 0 ] && echo "Commit aborted!" exit 1
exit 0
