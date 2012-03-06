from ...formats import FORMAT_INI
from ...config import Config
from .iniConfigSection import IniConfigSection

try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

class IniConfig(Config):
  def __init__(self):
    super(IniConfig, self).__init__(FORMAT_INI)

  def loadFromFile(self, inputFile):
    self.parser = ConfigParser()
    self.parser.readfp(inputFile)

  def getChildren(self):
    out = {}
    for section in self.parser.sections():
      out[section] = IniConfigSection(section, self.parser)
    return out

  def __getattr__(self, attributeName):
      return self.__getSectionOrRaise__(attributeName, AttributeError)

  def __getitem__(self, attributeName):
      return self.__getSectionOrRaise__(attributeName, IndexError)

  def __getSectionOrRaise__(self, attributeName, exceptionType):
    if self.parser.has_section(attributeName):
      return IniConfigSection(attributeName, self.parser)
    raise exceptionType('No section named [%s]', attributeName)

