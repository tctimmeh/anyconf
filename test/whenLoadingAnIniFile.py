import string, random

import sys
if sys.version_info[0] >= 3:
  from configparser import ConfigParser
  from io import StringIO
else:
  from ConfigParser import ConfigParser
  from StringIO import StringIO

from testHelpers import uniqStr

import anyconf

class WhenLoadingAnIniFile:
  def setup_method(self, method):
    self.configLoader = anyconf.ConfigLoader()
  
  def loadConfigWithContent(self, content):
    fileObj = StringIO(content)
    return self.configLoader.load(fileObj, anyconf.FORMAT_INI)

  def testThatConfigObjectHasConfigParserInstance(self):
    config = self.loadConfigWithContent('')
    assert isinstance(config.getParser(), ConfigParser)
    
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

  def testThatGettingChildrenOfConfigReturnsDictOfSections(self):
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

  def testThatConfigContainsSections(self):
    expected = uniqStr()
    config = self.loadConfigWithContent('[%s]' % expected)
    assert expected in config

  def testThatSectionsContainOptions(self):
    attrName = uniqStr()
    config = self.loadConfigWithContent(r'''[section]
%s = %s''' % (attrName, uniqStr()))

    assert attrName in config.section

