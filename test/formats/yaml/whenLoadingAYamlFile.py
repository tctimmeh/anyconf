import sys

if sys.version_info[0] >= 3:
  from io import StringIO
else:
  from StringIO import StringIO

import anyconf

class WhenLoadingAYamlFile:

  def testThatConfigObjectCanBeCreated(self):
    configLoader = anyconf.ConfigLoader()
    fileObj = StringIO('')
    configLoader.load(fileObj, anyconf.FORMAT_YAML)

  def testThatConfigObjectHasDictInstance(self):
    configLoader = anyconf.ConfigLoader()
    fileObj = StringIO('test:')
    config = configLoader.load(fileObj, anyconf.FORMAT_YAML)
    assert isinstance(config.getParser(), dict)