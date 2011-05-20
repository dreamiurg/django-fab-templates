from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='dpvt',
      version=version,
      description="Django project templates that support deployment to vagrant-managed virtual box",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django fabric vagrant',
      author='Dmitry Guyvoronsky',
      author_email='dmitry.guyvoronsky@gmail.com',
      url='http://demiurg.com.ua/dpvt',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'PasteScript>=1.3',
        'Cheetah',
      ],
      entry_points="""
      [paste.paster_create_template]
      vagrant_project=dpvt.pastertemplates:VagrantTemplate
      """,
      )
