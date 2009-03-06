# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='edrn.theme',
    version=version,
    description="Basic look-and-feel for the EDRN websites.",
    long_description=open("README.txt").read() + "\n" + open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='web zope plone theme edrn cancer',
    author='Andrew Hart',
    author_email='andrew.hart@jpl.nasa.gov',
    url='http://cancer.jpl.nasa.gov/products/edrn-theme',
    download_url='http://oodt.jpl.nasa.gov/dist/edrn-theme',
    license='Proprietary',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edrn'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points={},
)
