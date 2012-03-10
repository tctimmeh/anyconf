import pytest

import sys
if sys.version_info[0] >= 3:
  from io import StringIO
else:
  from StringIO import StringIO

import anyconf

def pytest_generate_tests(metafunc):
  if "fileFormat" in metafunc.funcargnames:
    metafunc.parametrize("fileFormat", anyconf.Formats)

class WhenLoadingAnIniFile:
  def setup_method(self, method):
    self.configLoader = anyconf.ConfigLoader()

  def getSampleConfig(self, fileFormat):
    sample = ''
    if fileFormat == anyconf.FORMAT_XML:
      sample = '<test />'
    return StringIO(sample)

  def loadConfig(self, fileFormat):
    fileObj = self.getSampleConfig(fileFormat)
    config = self.configLoader.load(fileObj, fileFormat)
    return config

  def testThatConfigObjectIsReturned(self, fileFormat):
    config = self.loadConfig(fileFormat)
    assert isinstance(config, anyconf.Config)

  def testThatReturnedObjectReportsCorrectFormat(self, fileFormat):
    config = self.loadConfig(fileFormat)
    assert config.getFormat() == fileFormat

