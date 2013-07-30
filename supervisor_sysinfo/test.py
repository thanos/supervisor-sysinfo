import xmlrpclib,pprint, json
from rpcinterface import API_VERSION, SysInfoNamespaceRPCInterface

rpc_proxy =  xmlrpclib.ServerProxy('http://very_safe:very_safe@127.0.0.1:9002')
print "TESTING VERSION"
assert rpc_proxy.sysinfo.getAPIVersion() == API_VERSION
print "TESTING rpc_proxy.sysinfo.ps()"
ps_list = rpc_proxy.sysinfo.ps()
assert ps_list and type(json.loads(ps_list)) == type({})
pprint.pprint(json.loads(ps_list))
#pprint.pprint(SysInfoNamespaceRPCInterface(None).sysInfo())
print "TESTING rpc_proxy.sysinfo.sysInfo()"
sysInfo =  rpc_proxy.sysinfo.sysInfo()

assert sysInfo and type(json.loads(sysInfo)) == type({})
pprint.pprint(json.loads(sysInfo))