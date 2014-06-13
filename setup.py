#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='relengapi-example',
      version='0.1',
      description='Example',
      author='example',
      author_email='example@mozilla.com',
      url='https://github.com/ianconnolly/build-relengapi-example',
      packages=find_packages(),
      namespace_packages=['relengapi', 'relengapi.blueprints'],
      entry_points={
          "relengapi_blueprints": [
              'example = relengapi.blueprints.example:bp',
          ],
      },
      package_data={
          'relengapi.blueprints.example': [
              'templates/*.html',
              'static/js/*.js',
              'static/css/*.css',
          ],
      },

      install_requires=[
          'Flask',
          'relengapi',
      ],
      license='MPL2',
      extras_require={
          'test': [
              'nose',
              'mock'
          ]
      })
