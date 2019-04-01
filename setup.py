from setuptools import setup, find_packages
from os import path
import attack


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='attack',
    version=attack.__VERSION__,
    description='A Penetration Testing Framework for hacker\'s !',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/th3hacker/attack',
    author='th3hacker',
    author_email='th3hacker@pwned.band',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='pentest infosec',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.6.*, <4',
    install_requires=[],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'attack=attack:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/th3hacker/attack/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'https://saythanks.io/to/th3hacker',
        'Source': 'https://github.com/th3hacker/attack/',
    },
)
