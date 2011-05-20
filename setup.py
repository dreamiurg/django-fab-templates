from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name = 'django-fab-templates',
      version = version,
      description = "Django project templates that support fabric-style deployment (vagrant+ubuntu, webfaction)",
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction = list_classifiers
      keywords = ['django', 'fabric', 'vagrant', 'template',
                  'project', 'html5', 'boilerplate', 'vm', 'virtualbox', 'paster'],
      author = 'Dmitry Guyvoronsky',
      author_email = 'dmitry.guyvoronsky@gmail.com',
      url = '',
      license = 'MIT',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      include_package_data = True,
      zip_safe = False,
      install_requires = [
        'setuptools',
        'PasteScript>=1.3',
        'Cheetah',
      ],
      entry_points = """
      [paste.paster_create_template]
      vagrant_project = django_fab_templates.pastertemplates:VagrantTemplate
      """,
      )
