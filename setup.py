#!/usr/bin/env python

#- * -coding: utf - 8 - * -
from setuptools import setup
# trying to fix ReStructured Text on PyPi, not exactly
# working(possibly needs to be stricter ? )


def readme():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except:
        with open('README.md') as f:
            return f.read()

setup(name = 'congredi',
    version = '0.0.2',
    description = 'BASE representation-of-law-via-cryptography protocol',
    long_description = readme(),
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Topic :: Security :: Cryptography'
    ],
    keywords = 'STV Single Transferable Voting Crypto Twisted',
    url = 'https://github.com/thetoxicarcade/congredi',
    author = 'Cameron Whiting',
    author_email = 'thetoxicarcade@gmail.com',
    license = 'GPL3',
    install_requires = [
        'twisted',
        'stem',
        'jwt',
        'twisted>=16.6.0',
        'PGPy>=0.4.0',
        'fernet>=1.0.1',
        'profanity>=1.1',
        'entropy>=0.9',
        'pycld2>=0.31',
        'chardet>=2.3.0',
        'stem>=1.5.3',
        'flask>=0.11.1',
        'urwid>=1.3.1',
        'txredisapi>=1.4.4',
        'py-gfm>=0.1.3',
        'pyyaml',
        'unidiff',
        'patch>=1.16',
        'redlock>=1.2.0',
        'jwt>=0.3.2',
        'neo4j-driver>=1.0.2'
    ],
    entry_points = {
        'console_scripts': [
            'congredi=congredi.main.options:run'
        ],
    },
    include_package_data = True,
    packages = ['congredi'],#,'docs'],
    package_data = {
        'delegito': ['*'],
        'docs': ['*/*'],
    },
    test_suite = 'nose2.collector.collector',
    tests_require = [
        'nose2',
        'setuptools-lint',
        'pylint'
    ],
    zip_safe = False
)# python setup.py register sdist upload
