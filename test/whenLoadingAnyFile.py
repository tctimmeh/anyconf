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
    self.fileObj = StringIO('')

  def testThatConfigObjectIsReturned(self, fileFormat):
    config = self.configLoader.load(self.fileObj, fileFormat)
    assert isinstance(config, anyconf.Config)

  def testThatReturnedObjectReportsCorrectFormat(self, fileFormat):
    config = self.configLoader.load(self.fileObj, fileFormat)
    assert config.getFormat() == fileFormat
    
