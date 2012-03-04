from __future__ import unicode_literals

import string, random
import pytest
from io import StringIO

try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

import anyconf

def uniqStr():
  return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))

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
