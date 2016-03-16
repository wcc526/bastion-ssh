****************************************
Bastion SSH: Bastion host for SSH
****************************************

Bastion SSH is designed for protecting,monitoring and accessing multiple SSH resources.

-----

|pypiv| |pypidm| |doc| |codeclimate| |travis_build| |appveyor_build| |coverage| |codecov| |gitter| |bitdeli| |license| |wheel|

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

.. |codecov| image:: https://codecov.io/github/wcc526/bastion-ssh/coverage.svg?branch=master
    :target: https://codecov.io/github/wcc526/bastion-ssh/?branch=master
    :alt: CodeCov coverage

.. |travis_build| image:: https://img.shields.io/travis/jkbrzt/httpie/master.svg?style=flat-square&label=unix%20build
    :target: https://travis-ci.org/wcc526/bastion-ssh
    :alt: Build status of the master branch on Mac/Linux

.. |appveyor_build| image:: https://ci.appveyor.com/api/projects/status/nmofap1c2xh72hs7?svg=true
    :target: https://ci.appveyor.com/api/projects/status/nmofap1c2xh72hs7/branch/master
    :alt: Build status of the master branch on appveyor

.. |gitter| image:: https://badges.gitter.im/wcc526/bastion-ssh.svg
    :target: https://gitter.im/wcc526/bastion-ssh
    :alt: Chat on Gitter

.. |bitdeli| image:: https://d2weczhvl823v0.cloudfront.net/wcc526/bastion-ssh/trend.png
     :target: https://bitdeli.com/free
     :alt: Bitdeli badge

.. |license| image:: https://img.shields.io/pypi/l/bastion_ssh.svg
     :target: https://pypi.python.org/pypi/bastion_ssh
     :alt: license

.. |doc| image:: https://readthedocs.org/projects/bastion-ssh/badge/?version=latest
    :target: http://bastion-ssh.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. |codeclimate| image:: https://codeclimate.com/github/wcc526/bastion-ssh/badges/gpa.svg
    :target: https://codeclimate.com/github/wcc526/bastion-ssh
    :alt: Code Climate

.. |wheel| image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/bastion_ssh/
    :alt: wheel
