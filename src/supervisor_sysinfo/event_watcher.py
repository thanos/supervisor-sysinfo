import sys
from supervisor import childutils
	
def write_stdout(s):
  sys.stdout.write(s)
  sys.stdout.flush()
  
  
def write_stderr(s):
  sys.stderr.write(s)
  sys.stderr.flush()

  
class EventWatcher(object):
  def run(self):
    while True:
      write_stdout('READY\n')
      # read header line and print it to stderr
      line = sys.stdin.readline()
      write_stderr(line)
      headers = dict([ x.split(':') for x in line.split() ])
      data = sys.stdin.read(int(headers['len']))
      self.process(headers, data)
      write_stdout('RESULT 2\nOK')

        
        
  def process(self, headers, data):
    write_stderr('pheader-> %s' % headers)
    write_stderr('pdata-> %s' % data)