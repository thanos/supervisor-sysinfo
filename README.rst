========
Overview
========



a supervisor rpc extension for obtaining the hosts system and process information plus a supervisor event monitor to
collect system stats and post them to a REST endpoint.

* Free software: BSD license

Installation
============

::

    pip install git+https://github.com/thanos/supervisor-sysinfo.git

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

  [eventlistener:monitor]
  command=supervisor_monitor http://some_end_point.com:7000/monitor
  events= TICK_60



Usage
=====

You can look at the test code but effectively you need to do this::

	import xmlrpclib,pprint, json

	rpc_proxy =  xmlrpclib.ServerProxy('http://very_safe:very_safe@127.0.0.1:9002')

	ps_list = json.loads(rpc_proxy.sysinfo.ps())
	pprint.pprint(ps_list)

	sysInfo =  json.loads(rpc_proxy.sysinfo.sysInfo())
	pprint.pprint(sysInfo)
  

Development
===========

To run the all tests run::

    tox
