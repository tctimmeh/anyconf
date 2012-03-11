import sys
if sys.version_info[0] >= 3:
  from configparser import ConfigParser
else:
  from ConfigParser import ConfigParser

from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenLoadingAnIniFile(IniFixture):
  def setup_method(self, method):
    super(WhenLoadingAnIniFile, self).setup_method(method)

  def testThatConfigObjectHasConfigParserInstance(self):
    config = self.loadConfigWithContent('')
    assert isinstance(config.getParser(), ConfigParser)

  def testThatGettingChildrenOfConfigReturnsDictOfSections(self):
    expected = []
    data = ''
    for i in range(5):
      sectionName = uniqStr()
      data += '[%s]\n' % sectionName
      expected.append(sectionName)

    config = self.loadConfigWithContent(data)

    actual = config.getChildren().keys()
    for i in range(5):
      assert expected[i] in actual

  def testThatConfigContainsSections(self):
    expected = uniqStr()
    config = self.loadConfigWithContent('[%s]' % expected)
    assert expected in config


