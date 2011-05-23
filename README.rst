django-fab-templates is set of start templates for Django projects. All of these templates support automated Django project deployment with help of `Fabric`_. Feel free to use them as is or tweak them to fit your needs.

Kudos to:

* Gareth Rushgrove and his `django-project-templates`_ for inspiration
* Colin Copeland for his introduction to `basic Django deployment with virtualenv, fabric, pip and rsync <http://www.caktusgroup.com/blog/2010/04/22/basic-django-deployment-with-virtualenv-fabric-pip-and-rsync/>`_

Please submit bugs and improvements as `GitHub issues <https://github.com/dreamiurg/django-fab-templates/issues>`_ or send them to dmitry.guyvoronsky@gmail.com.

Quick Start
===========

Here is quick primer on creation of new Django project (mysql+south+html5boilerplate) that supports deployment to vagrant-managed virtual box.

First, install everything::

    $ pip install django-fab-templates
    $ gem install vagrant
    $ vagrant box add base http://files.vagrantup.com/lucid32.box
    
Then create new Django project, boot and configure vagrant box::

    $ paster create -t vagrant_project my_project
    $ cd my_project
    $ vagrant up

Finally set up your project on virtual vagrant box and test it::

    $ fab vagrant setup
    $ curl -I http://localhost:8080/

Features
========

All project templates have the following in common:

* Automated deployment with help of `Fabric`_ command-line tool is supported
* Excellent `html5 boilerplate template <http://html5boilerplate.com>`_ is used as a base for html+css+js
* SQLite and MySQL are used as default db backends
* Database scheme and data migrations are managed by `South`_
* Multiple configurations (development/staging/production) and local setting overrides are supported

.. _common:

The following major ``fab`` commands are supported in all projects:

* **Webserver manipulation**
    * apache_restart - Restarts apache
    * apache_start - Starts apache
    * apache_stop - Stops apache
    * maintenance_off - Turn maintenance mode off
    * maintenance_on - Turn maintenance mode on
* **Database**
    * create_database - Create database and db user
    * drop_database - Create database and db user
    * populate_database - Create initial database scheme and load initial data
    * migrate - Migrate database scheme and data


vagrant_project
---------------

This project template simplifies Django project development and testing on vagrant-managed virtual box. It uses 32-bit Ubuntu 10.04.2 LTS (Lucid Lynx) release (codename ``lucid32``). Of course you operating system of your choice, just keep in mind you may need to tweak Chef settings in `Vagrantfile`_.

    **Hint**
    
    `Vagrant`_ is an amazing tool for managing virtual machines via a simple to use command line interface. With a simple ``vagrant up`` you can be working in a clean environment based on a standard template. You will need to install vagrant, download ``lucid32`` box and boot up vagrant by running::
    
    $ gem install vagrant
    $ vagrant box add base http://files.vagrantup.com/lucid32.box
    $ vagrant init
    $ vagrant up
    
    Please refer to `Getting Started with Vagrant <http://vagrantup.com/docs/getting-started/index.html>`_ manual for details.
    
The following ``fab`` commands are supported in addition to common_ ones:

* **General commands**
    * setup - Setup a fresh virtualenv, install everything we need
    * destroy_world - Removes everything
    
Example::

    $ paster create -t vagrant_project my_project
    $ cd my_project
    $ vagrant up
    $ fab vagrant setup


Dependencies
============

django-fab-templates requires the following python packages:

* `setuptools <http://pypi.python.org/pypi/setuptools>`_ - no comments
* `PasteScript <http://pypi.python.org/pypi/PasteScript>`_ - pluggable command-line frontend, including commands to setup package file layouts
* `Cheetah <http://pypi.python.org/pypi/Cheetah>`_ - a template engine and code generation tool
* `Fabric`_ - command-line automation tool
* `Jinja2 <http://jinja.pocoo.org/docs/>`_ - modern and designer friendly templating language for Python

Installation
============

From `pypi <http://pypi.python.org/pypi/django-fab-templates>`_::

    $ pip install django-fab-templates

or::

    $ easy_install django-fab-templates

or clone from `GitHub <https://github.com/dreamiurg/django-fab-templates>`_ and install manually::

    $ git clone git://github.com/dreamiurg/django-fab-templates.git
    $ cd django-fab-templates
    $ sudo python setup.py install

Usage
=====
To see list of available project templates::

    $ paster create --list-templates
    
To generate Django project template::

    $ paster create -t <template_name> <project_name>


.. _fabric: http://fabfile.org
.. _vagrant: http://vagrantup.com/
.. _south: http://south.aeracode.org/docs/about.html
.. _django-project-templates: http://pypi.python.org/pypi/django-project-templates/
.. _Vagrantfile: https://github.com/dreamiurg/django-fab-templates/blob/master/src/django_fab_templates/templates/vagrant_project/Vagrantfile
