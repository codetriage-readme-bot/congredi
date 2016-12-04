# WARNING - sync congredi/setup.py and congredi/delegito/setup.py
from setuptools import setup
def readme():
	with open('README.md') as f:
		return f.read()
setup(name='congredi',
	version='0.1',
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
	packages=['congredi'],
	install_requires=[
		'flask',
		'pymongo',
		'PGPy',
		'stem',
		'pyjwt'
		],
	include_package_data=True,
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