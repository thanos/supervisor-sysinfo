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

===============
supervisor-sysinfo
===============

a supervisor rpc extension for obtaining the hosts system and process information.


Requirements
============


* Python 2.7+
* supervisor 3.0+
* psutil




Why 
===

I use supervisor on many of my servers for control and monitoring and I needed a way to interrogate the sevrers for top, df and ps type information. Rather than have my own status server I've extended supervisor's XML-RPC api  to offer two new functions:
  * sysinfo.ps which returns a dictionary keyed by pid of the output of ps aux.
  * sysinfo.sysInfo which reruns cpu, memory and disk usage information.
  Both functions return json strings. I do this as a work around the 32-bit int limitation of the XML-RPC standard.



Installation
============

Use the usual ways::
    
     pip install git+https://github.com/thanos/supervisor-sysinfo.git





Setup
=====

In your supervisor.conf file setup::

	[inet_http_server]
	port = *:9002
	username = very_safe
	password = very_safe

Uncomment::
	
	[rpcinterface:supervisor]
	supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

Add::

	[rpcinterface:sysinfo]
	supervisor.rpcinterface_factory = supervisor_sysinfo.rpcinterface:make_sysinfo_rpcinterface







Usage
=====

You can look at the test code but effectively you need to do this::

	import xmlrpclib,pprint, json

	rpc_proxy =  xmlrpclib.ServerProxy('http://very_safe:very_safe@127.0.0.1:9002)

	ps_list = json.loads(rpc_proxy.sysinfo.ps())
	pprint.pprint(ps_list)

	sysInfo =  json.loads(rpc_proxy.sysinfo.sysInfo())
	pprint.pprint(sysInfo)
  

Development
===========

To run the all tests run::

    tox
