try:
    from setuptools import setup
except:
    from distutils.core import setup

config = { 
	'description': 'Test2 is for seeing if I can make a project that installs and has a script to run',
	'author' : 'Brian DeBelle',
	'url' : 'URL to get it at.',
	'download_url' : 'Where to download it.',
	'author_email' : 'brian[dot]debelle[at]gmail[dot]com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['test2'], 
	'scripts' : ['bin/testscript.py'],
	'name' : 'test2'
}

setup(**config)



