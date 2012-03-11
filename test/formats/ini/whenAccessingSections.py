from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenAccessingSections(IniFixture):
  def setup_method(self, method):
    super(WhenAccessingSections, self).setup_method(method)

  def testThatSectionsArePropertiesOfConfig(self):
    expected = uniqStr()
    config = self.loadConfigWithContent('[%s]' % expected)
    assert hasattr(config, expected)

  def testThatConfigDoesNotHavePropertiesForSectionsNotInConfig(self):
    config = self.loadConfigWithContent('[section]')
    assert not hasattr(config, uniqStr())

  def testThatSectionsAreAvailableAsDictItems(self):
    expected = uniqStr()
    config = self.loadConfigWithContent('[%s]' % expected)
    assert config[expected] is not None

  def testThatGettingChildrenOfSectionReturnsDictOfOptions(self):
    expected = {}
    data = '[section]\n'
    for i in range(5):
      optionName = uniqStr()
      optionValue = uniqStr()
      data += '%s = %s\n' % (optionName, optionValue)
      expected[optionName.lower()] = optionValue

    config = self.loadConfigWithContent(data)

    actual = config.section.getChildren()
    assert actual == expected


