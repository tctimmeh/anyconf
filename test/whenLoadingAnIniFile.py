from __future__ import unicode_literals

import pytest
from io import StringIO

try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

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
    expected = 'section'
    config = self.loadConfigWithContent('[%s]' % expected)
    assert hasattr(config, expected)

  def testThatConfigDoesNotHavePropertiesForSectionsNotInConfig(self):
    config = self.loadConfigWithContent('[section]')
    assert not hasattr(config, 'somethingelse')

  def testThatSectionsAreAvailableAsDictItems(self):
    expected = 'section'
    config = self.loadConfigWithContent('[%s]' % expected)
    assert config[expected] is not None
