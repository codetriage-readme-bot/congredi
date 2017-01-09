#!/bin/bash
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
    echo "running autopep8 formating..."
    autopep8 -rvi congredi
}
pyc(){
    echo "removing *.pyc..."
    find congredi/ -type f -name "*.pyc" -delete
}
check(){
    echo "linting..."
    pylint congredi
    echo "testing..."
    green congredi
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
case $1 in
    "requires")
        requires
        ;;
    "clean")
        clean
        ;;
    "pyc")
        pyc
        ;;
    "check")
        check
        ;;
    "build")
        build
        ;;
    "install")
        install
        ;;
    *)
        echo "commands are 'requires','clean','pyc','check','build', & 'install'."
        echo "in addition, you can run python3 via 'vbuild' and 'v3'"
        echo "running them all, now"
        requires
        clean
        check
        build
        install
        pyc
esac