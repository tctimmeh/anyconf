from __future__ import unicode_literals

import pytest
from io import StringIO
import anyconf

@pytest.mark.parametrize(("fileFormat"), anyconf.Formats)
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
    
