from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='Soracom',
      version=version,
      description="SORACOM SDK for Python",
      long_description="SORACOM provides sets of APIs to control their IoT platform service. This package will let you call SORACOM API from your python program.",
      classifiers=[
	    
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='soracom',
      author='MATSUI, Motokatsu',
      author_email='j3tm0t0@gmail.com',
      url='https://github.com/j3tm0t0/soracom-python',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
