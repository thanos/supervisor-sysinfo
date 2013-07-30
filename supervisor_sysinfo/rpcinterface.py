from supervisor.supervisord import SupervisorStates
from supervisor.xmlrpc import Faults
from supervisor.xmlrpc import RPCError
import subprocess, psutil

API_VERSION = '0.1'

class SysInfoNamespaceRPCInterface:
    """ A Supervisor RPC interface that provides the ability 
    to cache abritrary data in the Supervisor instance as key/value pairs.
    """

    def __init__(self, supervisord):
        self.supervisord = supervisord

    def _update(self, text):
        self.update_text = text # for unit tests, mainly

        state = self.supervisord.get_state()

        if state == SupervisorStates.SHUTDOWN:
            raise RPCError(Faults.SHUTDOWN_STATE)

        
    # RPC API methods

    def getAPIVersion(self):
        """ Return the version of the RPC API used by supervisor_cache

        @return string  version
        """
        self._update('getAPIVersion')
        return API_VERSION

    def ps(self):
        """ Return keys for all data stored in the cache

        @return  array   An array of strings representing cache keys
        """
        self._update('ps')
        processes ={}
        lines = subprocess.check_output(["ps", "aux"]).split("\n")[1:]
        for line in lines:
            line = line.strip()
            if line:
                row  = line.split()
                user, pid, cpu, mem, vsz, rss, tt, stat, started, time = row[:10]
                command = ' '.join(row[10:])
                processes[pid] = dict(user=user,  cpu=cpu, mem =mem, vsz=vsz, rss=rss, tt=tt, stat= stat, started = started, time=time, command=command)
        return processes


    def sysInfo(self):
        def extract(obj, *args):
            def norm(x):
                 if type(x) == type(1):
                        return  float(x) 
                 return x
            return dict([(arg, norm(getattr(obj, arg))) for arg in args])
        data ={}
        data['cpu_percent'] = psutil.cpu_percent(interval=1, percpu=False)
        data['cpu_times'] = extract(psutil.cpu_times(percpu=False), 'user', 'nice', 'system', 'idle')
        data['phymem_usage'] = extract(psutil.phymem_usage(), 'total', 'used', 'free', 'percent')
        disk_partitions=[]
        data['disk_partitions'] = [dict( partition_info = extract(partition, 'mountpoint', 'device'), 
                                        disk_usage = extract(psutil.disk_usage(partition.mountpoint), 'total', 'used', 'free', 'percent')) 
                                        for partition in psutil.disk_partitions(all=False)]
        return data

def make_sysinfo_rpcinterface(supervisord, **config):
    return SysInfoNamespaceRPCInterface(supervisord)
