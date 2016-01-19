from event_watcher import EventWatcher,write_stderr


class Monitor(EventWatcher):
  def __init__(self,  end_point):
    super(Monitor, self).__init__()
    self.end_point = end_point

    
if __name__ == '__main__':
  import sys
  Monitor(sys.argv[1]).run()
    