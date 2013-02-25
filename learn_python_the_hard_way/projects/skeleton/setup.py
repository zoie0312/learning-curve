try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Test Project',
	'author': 'who',
	'url': 'www.xxx.xxx.xxx',
	'download_url': 'github.com/xxx/xxx',
	'author_email': 'xxx@000.xxx.000',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['testproject'],
	'scripts': [],
	'name': 'mytestproject'
}

setup(**config)

 