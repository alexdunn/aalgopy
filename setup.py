"""Module information for aalgopy."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Algorithms Written in Python',
    'author': 'Xander Dunn',
    'url': 'https://github.com/xanderdunn/aalgopy',
    'download_url': 'https://github.com/xanderdunn/aalgopy',
    'author_email': 'xander.dunn@icloud.com',
    'version': '0',
    'install_requires': ['pytest', 'pytest-cov', 'coveralls', 'bitarray', 'numpy', 'nltk', 'scikit-learn'],
    'packages': ['aalgo'],
    'scripts': [],
    'name': 'aalgo'
}

setup(**config)
