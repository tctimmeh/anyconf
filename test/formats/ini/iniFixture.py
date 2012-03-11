import sys
if sys.version_info[0] >= 3:
  from io import StringIO
else:
  from StringIO import StringIO

import anyconf

class IniFixture(object):
  def setup_method(self, method):
    self.configLoader = anyconf.ConfigLoader()

  def loadConfigWithContent(self, content):
    fileObj = StringIO(content)
    return self.configLoader.load(fileObj, anyconf.FORMAT_INI)

