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
    find . -type d -exec chmod 755 {} \;
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
v3works(){
    green congredi.auth congredi.extra congredi.storage congredi.term congredi.tests \
    congredi.utils congredi.algos.test.test_router congredi.crypto.test.test_hash \
    congredi.crypto.test.test_kdf congredi.crypto.test.test_threshold
}
v3breaks(){
    v3
    green congredi.algos.test.test_diff congredi.algos.test.test_router \
    congredi.crypto.test.test_AES congredi.crypto.test.test_padding    
    v2
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
    "vbuild")
        vbuild
        ;;
    "v3")
        v3
        ;;
    "v2")
        v2
        ;;
    "v3works")
        v3works
        ;;
    "v3breaks")
        v3breaks
        ;;
    *)
        echo "commands are 'requires','clean','pyc','check','build', & 'install'."
        echo "python3 compat via vbuild, v3, v2, v3works, & v3breaks"
        echo "running the python2 commands..."
        requires
        clean
        check
        build
        install
        pyc
esac