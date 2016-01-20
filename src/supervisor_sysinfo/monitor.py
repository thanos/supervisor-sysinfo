import requests
import socket
import datetime

from event_watcher import EventWatcher,write_stderr

from sys_info import ps, sys_info

class Monitor(EventWatcher):
  def __init__(self,  end_point):
    super(Monitor, self).__init__()
    self.end_point = end_point
    
  def process(self, headers, data):
    data = {
      'ps': ps(),
      'sys': sys_info(),
      'host': socket.gethostbyname(socket.gethostname()),
      'timestamp': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    res = requests.post(self.end_point, json=data)
    write_stderr('end_point-> %s' % self.end_point)
    write_stderr('res-> %s' % res)
    #write_stderr('data-> %s' % data)
    
if __name__ == '__main__':
  import sys
  Monitor(sys.argv[1]).run()
    