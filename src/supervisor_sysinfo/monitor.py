from event_watcher import EventWatcher,write_stderr


class Monitor(EventWatcher):
  def __init__(self,  end_point, interval ='TICK_60'):
    super(Monitor, self).__init__()
    self.interval = interval
    self.end_point = end_point
    
  def interestedIn(self, headers):
    return headers['eventname'] == self.interval
  
  def process(self, headers, pheader, pdata):
    write_stderr('pheader-> %s' % pheader)
    write_stderr('pdata-> %s' % pdata)
    
if __name__ == '__main__':
  import sys
  Monitor(sys.argv[1], sys.argv[2]).run()
    