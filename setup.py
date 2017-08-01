from setuptools import setup
import distutils.command.sdist

import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

VERSION = __import__('dxldomaintoolsclient').get_version()

dist = setup(
    # Package name:
    name="dxldomaintoolsclient",

    # Version number:
    version=VERSION,

    # Requirements
    install_requires=[
        "dxlbootstrap",
        "dxlclient"
    ],

    # Package author details:
    author="",

    # License
    license="",

    # Keywords
    keywords=[],

    # Packages
    packages=[
        "dxldomaintoolsclient",
    ],

    # Details
    url="",

    description="",

    long_description=open('README').read(),

    classifiers=[
        "Programming Language :: Python"
    ],
)
