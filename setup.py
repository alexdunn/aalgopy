try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


config = {
    'description': 'Algorithms Written in Python',
    'author': 'Alex Dunn',
    'url': 'https://github.com/alexdunn/aalgopy',
    'download_url': 'Where to download it.',
    'author_email': 'dunn.alex@icloud.com',
    'version': '0',
    'install_requires': ['pytest', 'pytest-cov', 'coveralls'],
    'packages': ['aalgo'],
    'scripts': [],
    'name': 'aalgo'
}

setup(**config)
