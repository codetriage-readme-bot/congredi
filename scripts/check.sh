#!/bin/sh
pylint congredi
nose2 congredi
#python setup.py build test lint bdist_wheel install
#python setup.py lint || echo "Code Quality failing..."

find congredi/ -type f -name "*.pyc" -delete -print
#mkdocs gh-deploy