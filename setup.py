import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()

setup(
    name="wikiclass",
    version="0.2.2",  # see wikiclass/__init__.py
    author="Aaron Halfaker / Morten Warncke-Wang",
    author_email="ahalfaker@wikimedia.org",
    description=("A library for performing automatic detection of assessment classes of Wikipedia articles."),
    license="MIT",
    url="https://github.com/halfak/wikiclass",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wikiclass=wikiclass.wikiclass:main'
        ],
    },
    long_description=read('README.md'),
    install_requires=list(requirements('requirements.txt')),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering"
    ],
)
