****************************************
Bastion SSH: Bastion host for SSH
****************************************

Bastion SSH is designed for protecting,monitoring and accessing multiple SSH resources.

-----

|pypiv| |pypidm| |unix_build| |coverage| |gitter| |bitdeli|

-----

.. contents::
    :local:
    :depth: 1
    :backlinks: none

=============
Main Features
=============

* Monitor user's input

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

.. |unix_build| image:: https://img.shields.io/travis/jkbrzt/httpie/master.svg?style=flat-square&label=unix%20build
    :target: https://travis-ci.org/wcc526/bastion-ssh
    :alt: Build status of the master branch on Mac/Linux

.. |gitter| image:: https://badges.gitter.im/wcc526/bastion-ssh.svg
    :target: https://gitter.im/wcc526/bastion-ssh
    :alt: Chat on Gitter

.. |bitdeli| image:: https://d2weczhvl823v0.cloudfront.net/wcc526/bastion-ssh/trend.png
     :target: https://bitdeli.com/free
     :alt: Bitdeli badge
