try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = { 
	'description': 'My Project',
	'author' : 'Brian DeBelle',
	'url' : 'URL to get it at.',
	'download_url' : 'Where to download it.',
	'author_emial' : 'brian[dot]debelle[at]gmail[dot]com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : '[NAME]', 
	'scripts' : '[]',
	'name' : 'projectname'
}

setup(**config)



