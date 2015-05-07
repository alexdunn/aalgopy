[![Build Status](https://travis-ci.org/xanderdunn/aalgopy.svg?branch=master)](https://travis-ci.org/xanderdunn/aalgopy)
[![Coverage Status](https://coveralls.io/repos/alexdunn/aalgopy/badge.svg)](https://coveralls.io/r/alexdunn/aalgopy)
[![Code Climate](https://codeclimate.com/github/alexdunn/aalgopy/badges/gpa.svg)](https://codeclimate.com/github/alexdunn/aalgopy)
[![Code Health](https://landscape.io/github/xanderdunn/aalgopy/master/landscape.svg?style=flat)](https://landscape.io/github/xanderdunn/aalgopy/master)
[![Codacy Badge](https://www.codacy.com/project/badge/c8b2d51aa0934addb24e6a55ea55f95f)](https://www.codacy.com/app/worthless-trash-junk/aalgopy)

## About
This is a collection of algorithms written in Python 3.4.  Many of the algorithms are from the textbook *The Algorithm Design Manual*.

## Test
- `pip install -e .`
- `py.test`

## Tools

### Working Automatically
- Travis CI = Continuous integration that builds and runs the project every time commits are pushed to GitHub.
- Coveralls = Track how well the code is covered by unit tests. This is updated automatically by Travis CI.
- Landscape = Static analysis and code quality.
- Code Climate = Test coverage, style, quality, and security analysis.
- Codacy = Static analysis and code quality.
- pep8 = A linter and standards adherence tool.  I'm ignoring pep8's requirement that all lines of code are not to be longer than 80 characters.
- pyflakes = A linter. This is integrated into the IDE as I edit code.
- pylint = This is integrated into the IDE as I edit code.
- mccabe = A code complexity static analyzer.  This is integrated into the IDE as I edit code.

