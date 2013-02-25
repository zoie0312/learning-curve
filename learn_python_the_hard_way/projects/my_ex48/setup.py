try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My ex48 from "Learn Python The Hard Way"',
	'author': 'who',
	'url': 'www.xxx.xxx.xxx',
	'download_url': 'github.com/xxx/xxx',
	'author_email': 'xxx@000.xxx.000',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)

 