pip install -q -r requirements.txt nose2 setuptools-lint pylint
python setup.py build install 1>/dev/null
python setup.py bdist_wheel 1>/dev/null
python setup.py test 1>/dev/null
python setup.py lint || echo "Lint failed..."