# WARNING - sync congredi/setup.py and congredi/delegito/setup.py
from setuptools import setup
def readme():
	with open('README.md') as f:
		return f.read()
setup(name='delegito',
	version='0.1',
	description='Single Transferable Voting service',
	long_description='Delegito is the python module for an STV API called congredi.\
	This is currently a work in progress, so the Shuffle-Sum & Secure Secret Sharing\
	are not implemented as directly as need be. I\'m also terrible at interfaces...', #readme()
	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.7',
		'Operating System :: POSIX :: Linux',
		'Topic :: Security :: Cryptography'
		],
	keywords='STV Single Transferable Voting',
	url='https://github.com/thetoxicarcade/congredi',
	author='Cameron Whiting',
	author_email='thetoxicarcade@gmail.com',
	license='GPL3',
	packages=['delegito'],
	install_requires=[
		'flask',
		'pymongo',
		'PGPy',
		'stem',
		'pyjwt'
		],
	include_package_data=True,
	#https://tom-christie.github.io/articles/pypi/
	#http://stackoverflow.com/questions/15650331/how-to-include-package-sub-folders-in-my-project-distribution/28298339
	#packages = ['.','delegito','docs','security','service','tests'],
	#package_data={'delegito':['*'],'docs':['*/*'],},
	test_suite='nose2.collector.collector',
	tests_require=[
		'nose2',
		'setuptools-lint',
		'pylint'],
	zip_safe=False
	)
#python setup.py register sdist upload