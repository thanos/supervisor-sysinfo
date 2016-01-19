import unittest
from supervisor_sysinfo.sys_info import ps, sys_info

#def test_main():
#     assert main([]) == 0


class TestSequenceFunctions(unittest.TestCase):
  def test_sysinfo_ps(self):
    print "testing sysinfo.ps()"
    ps_list = ps()
    self.assertEqual(type(ps_list), type({}))
    
  def test_sysinfo_cpu_times(self):
    sysInfo =  sys_info()
    self.assertEqual(type(sysInfo['cpu_times']['user']), type(1.0))
    self.assertEqual(type(sysInfo['cpu_times']['system']), type(1.0))
    self.assertEqual(type(sysInfo['cpu_times']['idle']), type(1.0))
 

  def test_sysinfo_virtual_memory(self):
    print "testing sysinfo_virtual_memory.ps()"
    sysInfo =  sys_info()
    self.assertEqual(type(sysInfo['virtual_memory']['total']), type(8374149120L))
    self.assertEqual(type(sysInfo['virtual_memory']['used']), type(8374149120L))
    self.assertEqual(type(sysInfo['virtual_memory']['available']), type(8374149120L))
    self.assertEqual(type(sysInfo['virtual_memory']['percent']), type(1.0))
  
  
  def test_sysinfo_disk_partitions(self):
    print "testing sysinfo_disk_partitions.ps()"
    sysInfo =  sys_info()
    print sysInfo['disk_partitions']
    self.assertEqual(type(sysInfo['disk_partitions'][0]['disk_usage']['used']), type(0))
    self.assertEqual(type(sysInfo['disk_partitions'][0]['disk_usage']['total']), type(0))
    self.assertEqual(type(sysInfo['disk_partitions'][0]['disk_usage']['free']), type(0))
    self.assertEqual(type(sysInfo['disk_partitions'][0]['disk_usage']['percent']), type(0.0))
    self.assertEqual(type(sysInfo['disk_partitions'][0]['partition_info']['device']), type(''))
    self.assertEqual(type(sysInfo['disk_partitions'][0]['partition_info']['mountpoint']), type(''))
#       data['disk_partitions'] = [dict( partition_info = extract(partition, 'mountpoint', 'device'), 
#                                       disk_usage = add_inode_usage(partition.mountpoint, 
                                    # cextract(psutil.disk_usage(partition.mountpoint), 'total', 'used', 'free', 'percent'))) 
  
  def test_sysinfo_net_io(self):
    print "testing sysinfo_net_io.ps()"
    sysInfo =  sys_info()
    self.assertEqual(type(sysInfo['net_io']['bytes_sent']), type(0))
    self.assertEqual(type(sysInfo['net_io']['bytes_recv']), type(0))
    self.assertEqual(type(sysInfo['net_io']['packets_sent']), type(0))
    self.assertEqual(type(sysInfo['net_io']['packets_recv']), type(0))
    self.assertEqual(type(sysInfo['net_io']['errin']), type(0))
    self.assertEqual(type(sysInfo['net_io']['errout']), type(0))
    self.assertEqual(type(sysInfo['net_io']['dropin']), type(0))
    self.assertEqual(type(sysInfo['net_io']['dropout']), type(0))

    
  def test_sysinfo_boot_time(self):
    print "testing sysinfo_net_io.ps()"
    sysInfo =  sys_info()
    self.assertEqual(type(sysInfo['boot_time']), type(0.0))
    
    
  def test_sysinfo_users(self):
    print "testing sysinfo_net_io.ps()"
    sysInfo =  sys_info()
    self.assertEqual(type(sysInfo['users'][0]['name']), type(''))
    self.assertEqual(type(sysInfo['users'][0]['terminal']), type(''))
    self.assertEqual(type(sysInfo['users'][0]['host']), type(''))
    self.assertEqual(type(sysInfo['users'][0]['started']), type(0.0))
#       data['disk_partitions'] = [dict( partition_info = extract(partition, 'mountpoint', 'device'), 
#                                       disk_usage = add_inode_usage(partition.mountpoint, 
                                    # cextract(psutil.disk_usage(partition.mountpoint), 'total', 'used', 'free', 'percent'))) 
#                                       for partition in psutil.disk_partitions(all=False)]                                      for partition in psutil.disk_partitions(all=False)]

if __name__ == '__main__':
    unittest.main()                                                                                                                