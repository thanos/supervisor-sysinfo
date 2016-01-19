========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/supervisor-sysinfo/badge/?style=flat
    :target: https://readthedocs.org/projects/supervisor-sysinfo
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/thanos/supervisor-sysinfo.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/thanos/supervisor-sysinfo

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/thanos/supervisor-sysinfo?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/thanos/supervisor-sysinfo

.. |requires| image:: https://requires.io/github/thanos/supervisor-sysinfo/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/thanos/supervisor-sysinfo/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/supervisor_sysinfo.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/supervisor_sysinfo

.. |downloads| image:: https://img.shields.io/pypi/dm/supervisor_sysinfo.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/supervisor_sysinfo

.. |wheel| image:: https://img.shields.io/pypi/wheel/supervisor_sysinfo.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/supervisor_sysinfo

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/supervisor_sysinfo.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/supervisor_sysinfo

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/supervisor_sysinfo.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/supervisor_sysinfo


.. end-badges

a supervisor rpc extension for obtaining the hosts system and process information plus a supervisor event monitor to
collect system stats and post them to a REST endpoint.

* Free software: BSD license

Installation
============

::

    pip install supervisor_sysinfo

Documentation
=============

https://supervisor-sysinfo.readthedocs.org/

Development
===========

To run the all tests run::

    tox
