#!/usr/bin/env python

#- * -coding: utf - 8 - * -
from setuptools import setup, find_packages
# trying to fix ReStructured Text on PyPi, not exactly
# working(possibly needs to be stricter ? )


def readme():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except:
        with open('README.md') as f:
            return f.read()

setup(name='congredi',
      version='0.0.3',
      description='BASE representation-of-law-via-cryptography protocol',
      long_description=readme(),
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Operating System :: POSIX :: Linux',
          'Topic :: Security :: Cryptography'
      ],
      keywords='STV Single Transferable Voting Crypto Twisted',
      url='https://github.com/thetoxicarcade/congredi',
      author='Cameron Whiting',
      author_email='thetoxicarcade@gmail.com',
      license='GPL3',
      install_requires=[
          'chardet>=2.3.0',
          'entropy>=0.9',
          'klein>=16.12.0',
          'patch>=1.16',
          'profanity>=1.1',
          'py2neo>=3.1.2',
          'pycld2>=0.31',
          'pycryptodome>=3.4.3',
          'pyelliptic>=1.5.7',
          'py-gfm>=0.1.3',
          'pyjwt>=1.4.2',
          'python-vote-full>=1.0',
          'pyyaml',
          'redlock>=1.2.0',
          'stem>=1.5.3',
          'twisted>=16.6.0',
          'txredisapi>=1.4.4',
          'unidiff',
          'urwid>=1.3.1'
      ],
      entry_points={
          'console_scripts': [
              'congredi=congredi.term.run:run'
          ],
      },
      include_package_data=True,
      packages=find_packages(exclude=['.pyc','.md','.pdf']),
      #packages=['congredi'],  # ,'docs'],
      package_data={
          'delegito': ['*'],
          'docs': ['*/*'],
      },
      tests_require=[
          'setuptools-green',
          'green>=2.5.3',
          'setuptools-lint',
          'pylint'
      ],
      zip_safe=False
      )  # python setup.py register sdist upload
