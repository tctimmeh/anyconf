from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenAccessingOptions(IniFixture):
  def setup_method(self, method):
    super(WhenAccessingOptions, self).setup_method(method)

  def testThatValuesAreAvailableAsPropertiesOfASection(self):
    attrName = uniqStr()
    attrValue = uniqStr()
    config = self.loadConfigWithContent(r'''[section]
%s = %s''' % (attrName, attrValue))

    assert getattr(config.section, attrName) == attrValue

  def testThatSectionsDoNotHavePropertiesForValuesNotInConfig(self):
    config = self.loadConfigWithContent(r'''[section]
name = value''')
    assert not hasattr(config.section, uniqStr())

  def testThatValuesAreAvailableAsDictItemsOfSection(self):
    attrName = uniqStr()
    attrValue = uniqStr()
    config = self.loadConfigWithContent(r'''[section]
%s = %s''' % (attrName, attrValue))

    assert config.section[attrName] == attrValue

  def testThatSectionsContainOptions(self):
    attrName = uniqStr()
    config = self.loadConfigWithContent(r'''[section]
%s = %s''' % (attrName, uniqStr()))

    assert attrName in config.section


