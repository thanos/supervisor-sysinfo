import xmlrpclib,pprint, json
from rpcinterface import API_VERSION

import unittest

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.rpc_proxy =  xmlrpclib.ServerProxy('http://very_safe:very_safe@127.0.0.1:9002')
	
	def test_getAPIVersion(self):
		print "testing sysinfo.getAPIVersion()"
		self.assertEqual(self.rpc_proxy.sysinfo.getAPIVersion(), API_VERSION)
	
	def test_sysinfo_ps(self):
		print "testing sysinfo.ps()"
		ps_list = json.loads(self.rpc_proxy.sysinfo.ps())
		self.assertEqual(type(ps_list), type({}))
	
	def test_sysinfo_sysInfo(self):
		print "testing sysinfo.sysInfo()"
		#sysInfo =  json.loads(self.rpc_proxy.sysinfo.sysInfo())
		#self.assertEqual(type(sysInfo), type({}))

if __name__ == '__main__':
    unittest.main()