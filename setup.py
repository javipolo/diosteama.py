#!/usr/bin/env python

from setuptools import setup, find_packages
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

setup(name='diosteama',
      version='0.1',
      description='DiosTeAma amigos',
      author='Javi Polo',
      author_email='javipolo@drslump.org',
      maintainer='Javi Polo',
      maintainer_email='javipolo@drslump.org',
      packages=find_packages(),
      keywords='diosteama',
      scripts=['diosteama.py'],
      zip_safe=False)
