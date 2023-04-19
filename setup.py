#!/usr/bin/env python

from shutil import rmtree
from setuptools import setup, find_packages

setup(name='escodegen',
      version='0.0.1',
      description='ECMA Script generation from esprima AST.',
      url='https://github.com/synesenom/escodegen-python',
      author='Enys Mones',
      author_email='enys.mones@gmail.com',
      packages=find_packages(),
      install_requires=[
            'esutils==1.0.1',
      ])

# Clean-up
print('\nCleaning up.')
rmtree('escodegen.egg-info')
rmtree('build')
rmtree('dist')
