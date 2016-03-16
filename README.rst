****************************************
Bastion SSH: Bastion host for SSH
****************************************

Bastion SSH is designed for protecting,monitoring and accessing multiple SSH resources.

-----

|pypiv| |pypidm| |doc| |codeclimate| |code_health| |build| |coverage| |gitter|

-----

.. contents::
    :local:
    :depth: 1
    :backlinks: none

=============
Main Features
=============

* Monitor user's input

=============
ScreenShots
=============

.. image:: https://raw.githubusercontent.com/wcc526/bastion-ssh/master/docs/screenshots.gif
    :alt: ScreenShots
    :width: 679
    :height: 781
    :align: center


============
Installation
============

To install Bastion SSH, simply:

.. code-block:: bash

    $ pip install bastion_ssh

=====
Usage
=====

Hello World:

.. code-block:: bash

    $ bastion_ssh.py -H 192.168.0.1 -u root


.. |pypiv| image:: https://img.shields.io/pypi/v/bastion_ssh.svg
    :target: https://pypi.python.org/pypi/bastion_ssh
    :alt: Latest version released on PyPi

.. |pypidm| image:: https://img.shields.io/pypi/dm/bastion_ssh.svg
    :target: https://pypi.python.org/pypi/bastion_ssh
    :alt: Latest version released on PyPi

.. |coverage| image:: https://img.shields.io/coveralls/wcc526/bastion-ssh/master.svg
    :target: https://coveralls.io/r/wcc526/bastion-ssh?branch=master
    :alt: Test coverage

.. |build| image:: https://img.shields.io/travis/jkbrzt/httpie/master.svg
    :target: https://travis-ci.org/wcc526/bastion-ssh
    :alt: Build status of the master branch on Mac/Linux

.. |gitter| image:: https://badges.gitter.im/wcc526/bastion-ssh.svg
    :target: https://gitter.im/wcc526/bastion-ssh
    :alt: Chat on Gitter

.. |doc| image:: https://readthedocs.org/projects/bastion-ssh/badge/?version=latest
    :target: http://bastion-ssh.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. |codeclimate| image:: https://codeclimate.com/github/wcc526/bastion-ssh/badges/gpa.svg
    :target: https://codeclimate.com/github/wcc526/bastion-ssh
    :alt: Code Climate

.. |code_health| image:: https://landscape.io/github/wcc526/bastion-ssh/master/landscape.svg
    :target: https://landscape.io/github/wcc526/bastion-ssh/master
    :alt: Code Health
