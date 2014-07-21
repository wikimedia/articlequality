import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()

setup(
    name = "wikiclass",
    version = read('VERSION').strip(),
    author = "Aaron Halfaker / Morten Warncke-Wang",
    author_email = "ahalfaker@wikimedia.org",
    description = ("A library for performing automatic detection of assessment classes of Wikipedia articles."),
    license = "MIT",
    url = "https://github.com/halfak/Wiki-Class",
    packages = find_packages(),
    long_description = read('README.rst'),
    install_requires = requirements('requirements.txt'),
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
