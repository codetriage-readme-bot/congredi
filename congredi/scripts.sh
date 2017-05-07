#!/bin/bash
changelog(){
    echo changes by @$(whoami) at $(date +"%F %T %Z(%z)") >> changelog.txt
    echo $(git config user.name)" <"$(git config user.email)">" >> changelog.txt
    IFS=$'\n'
    for line in $(git status --porcelain); do
    	echo "* $line - <description>" >> changelog.txt
    done
    IFS=' '
    if [ -z $EDITOR ]; then
        read -p "\$EDITOR unset. enter editor to set: " editor
        export EDITOR=$editor
    fi
    $EDITOR changelog.txt
    git status
}
version(){
    echo "bumping version in setup.py to $1..."
    perl -pi -w -e "s/version='(.+)'/version='"$1"'/g;" setup.py
}
requires(){
    echo "installing build dependencies..."
    pip install -q autopep8 setuptools-green green setuptools-lint pylint
    echo "installing package requirements..."
    pip install -q -r requirements.txt
}
clean(){
    echo "cleaning from .gitignore options..."
    while read line; do
    	find . -name "$line" -prune -print -exec rm -r {} \;
    done < .gitignore;
    echo "removing executability from congredi/ folder..."
    chmod -x congredi/ -R
    find . -type d -exec chmod 755 {} \;
    echo "running autopep8 formating..."
    autopep8 -rvi congredi
    echo "after autopep8, your directory is..."
    git status
}
pyc(){
    echo "removing *.pyc..."
    find congredi/ -type f -name "*.pyc" -delete
}
lint(){
    echo "linting..."
    pylint congredi || return 1
}
runtest(){
    echo "testing..."
    green congredi -vvv || return 1
}
check(){
    lint
    runtest
}
build(){
    echo "building..."
    #mkdocs gh-deploy || echo "Docs failing..."
    python setup.py build bdist_wheel 1>/dev/null
}
install(){
    echo "installing..."
    sudo python setup.py install
}
vbuild(){
    pushd ~
        virtualenv 2to3 -p python3
    popd
}
v3(){
    source ~/2to3/bin/activate
}
v2(){
    deactivate
}
# everything should work, for now. Rewrite this if you need it.
# v3works(){
#     green congredi.auth congredi.extra congredi.storage congredi.term congredi.tests \
#     congredi.utils congredi.algos.test.test_router congredi.crypto.test.test_hash \
#     congredi.crypto.test.test_kdf congredi.crypto.test.test_threshold
# }
# v3breaks(){
#     green congredi.algos.test.test_diff congredi.algos.test.test_router \
#     congredi.crypto.test.test_AES congredi.crypto.test.test_padding    
# }
USAGE=$(cat <<END
Welcome to the utility scripts. Now with autocompletion!

source scripts.sh --option
    default:
        prepending $prefix is not required, i.e. \`$prefix version\` = \`version\`.
        $prefix set to 'congredi-scripts' by default.
    --rootless
        prepending $prefix is required.
    --short
        $prefix swaps from 'congredi-scripts' to 'cs'
    --quiet
        don't print the welcome message
    
Commands include:

    changelog - creates a changelog based on git diff --porcelain
    version - perl substitutes setup.py's version

    requires - runs pip install -r requirements.txt, among others

    clean - cleans tree, removes files, runs autopep8
    pyc - removes just pyc files
    check - runs pylint & green
        lint - runs pylint
        runtest - runs tests

    build - setup.py build
    install - setup.py install

    vbuild - builds virtualenv
    v3 - starts v3 virtualenv (cannot be used when sourced with --rootless)
    v2 - deactivates virtualenv (cannot be used when sourced with --rootless)

A good example is: (could probably even have travis run this)

    git add -A
    clean && check && v3 && runtest && v2 && pyc

END
)
congredi-scripts(){
    # function for renaming global functions if sourced...
    setcheck(){
        if [[ "$(type -t $1)" == "function" ]]; then
            $1
        else
            source $BASH_SOURCE --quiet
            $1
            cs unsetall
        fi
    }
    case $1 in
        "unsetall") unset changelog version requires clean pyc check build install vbuild v3 v2 ;;
        "version") setcheck version $2 ;;
        "help") echo "$USAGE" ;;
        "all")
            setcheck requires
            setcheck clean
            setcheck check
            setcheck build
            setcheck install
            setcheck pyc
            ;;
        *) setcheck $1 ;;
    esac
}

complete -W "changelog version requires clean pyc check lint runtest build install vbuild v3 v2" congredi-scripts
if [[ $0 != "$BASH_SOURCE" ]]; then
    cgprefix="congredi-scripts"
    cgrequired="not required."
    cgprint=1
    while [ $# -gt 0 ]; do
        arg=$1
        case $arg in
            --rootless)
                cs unsetall
                cgrequired="required."
            ;;
            --quiet)
                cgprint=0
            ;;
            --short)
                cs(){ congredi-scripts; }
                export cs
                complete -W "changelog version requires clean pyc check build install vbuild v3 v2" cs
                cgprefix="cs"
            ;;
        esac
        shift
    done
    if [[ $cgprint == 1 ]]; then
        echo "Congredi scripts enabled ($BASH_SOURCE). Appending" \'$cgprefix\' $cgrequired " Run '$cgprefix help' for more info."
    fi
else
    congredi-scripts
fi