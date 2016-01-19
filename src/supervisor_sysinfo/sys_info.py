

from supervisor.supervisord import SupervisorStates
from supervisor.xmlrpc import Faults
from supervisor.xmlrpc import RPCError
import subprocess, psutil, json, math, os, statvfs

def ps():
  """ Return keys for all data stored in the cache

  @return  json repr of a dict of process details keyed by pid.

  >>> ps()
     {
      u'30194': {u'command': u'/Users/thanos/supervisor-sysinfo/bin/python /Users/thanos/supervisor-sysinfo/bin/supervisord -c supervisor.conf',
                  u'cpu': u'0.0',
                  u'mem': u'0.1',
                  u'rss': u'5908',
                  u'started': u'5:21PM',
                  u'stat': u'Ss',
                  u'time': u'0:00.08',
                  u'tt': u'??',
                  u'user': u'thanos',
                  u'vsz': u'2448924'},
       u'30283': {u'command': u'python supervisor_sysinfo/test.py',
                  u'cpu': u'11.2',
                  u'mem': u'0.3',
                  u'rss': u'11008',
                  u'started': u'5:27PM',
                  u'stat': u'S+',
                  u'time': u'0:00.10',
                  u'tt': u's009',
                  u'user': u'thanos',
                  u'vsz': u'2444692'},
       u'30284': {u'command': u'ps aux',
                  u'cpu': u'0.0',
                  u'mem': u'0.0',
                  u'rss': u'620',
                  u'started': u'5:27PM',
                  u'stat': u'R',
                  u'time': u'0:00.00',
                  u'tt': u'??',
                  u'user': u'root',
                  u'vsz': u'2434820'},
       u'985': {u'command': u'/Applications/Utilities/Console.app/Contents/MacOS/Console -psn_0_381021',
                u'cpu': u'0.0',
                u'mem': u'0.4',
                u'rss': u'15532',
                u'started': u'Wed02PM',
                u'stat': u'S',
                u'time': u'11:25.89',
                u'tt': u'??',
                u'user': u'thanos',
                u'vsz': u'2745052'}}
  """
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





def sys_info():
      """
      @return   dict.


      >>> sysInfo()

      {u'cpu_percent': 3.0,
       u'cpu_times': {u'idle': 4105971.75,
                      u'nice': 0.0,
                      u'system': 55322.1,
                      u'user': 92921.92},
       u'disk_partitions': [{u'disk_usage': {u'free': 309265399808.0,
                                             u'percent': 69.0,
                                             u'total': 999345127424.0,
                                             u'used': 689817583616.0
                                             u'ipercent': 7.0, 
                                             u'ifree': 491028, 
                                             u'inodes': 524288},
                             u'partition_info': {u'device': u'/dev/disk0s2',
                                                 u'mountpoint': u'/'}}],
       u'phymem_usage': {u'free': 44892160,
                         u'percent': 73.5,
                         u'total': 4294967296,
                         u'used': 4240707584}}
      """
      def add_inode_usage(mountpoint, disk_usage):
          istats = os.statvfs(mountpoint)
          disk_usage['inodes'] =  istats[statvfs.F_FILES]
          disk_usage['ifree'] = istats[statvfs.F_FFREE]
          disk_usage['ipercent'] = math.ceil(float(100*(istats[statvfs.F_FILES]-istats[statvfs.F_FFREE]))/istats[statvfs.F_FILES]) if istats[statvfs.F_FILES] else 0
          return disk_usage

      def extract(obj, *args):
          return dict([(arg, getattr(obj, arg)) for arg in args])
      data ={}
      data['cpu_percent'] = psutil.cpu_percent(interval=1, percpu=False)
      data['cpu_times'] = extract(psutil.cpu_times(percpu=False), 'user', 'system', 'idle')
      data['virtual_memory'] = extract(psutil.virtual_memory(), 'total', 'used','available', 'free', 'percent')
      disk_partitions=[]
      data['disk_partitions'] = [dict( partition_info = extract(partition, 'mountpoint', 'device'), 
                                      disk_usage = add_inode_usage(partition.mountpoint, extract(psutil.disk_usage(partition.mountpoint), 'total', 'used', 'free', 'percent'))) 
                                      for partition in psutil.disk_partitions(all=True)]
      data['net_io'] = extract(psutil.net_io_counters(), 'bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv', 'errin', 'errout', 'dropin', 'dropout')
      data['boot_time'] = psutil.boot_time()
      data['users'] = [ extract(user, 'name', 'terminal','host', 'started')    for user in psutil.users()]
      
      return data
    
    
    
