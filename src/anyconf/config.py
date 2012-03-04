try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

class Config:
  def __init__(self, data, fmt):
    self.fmt = fmt

    self.parser = ConfigParser()
    self.parser.readfp(data)

  def getFormat(self):
      return self.fmt

  def getParser(self):
      return self.parser

  def getChildren(self):
    out = {}
    for section in self.parser.sections():
      out[section] = ConfigSection(section, self.parser)
    return out

  def __getattr__(self, attributeName):
      return self.__getSectionOrRaise__(attributeName, AttributeError)

  def __getitem__(self, attributeName):
      return self.__getSectionOrRaise__(attributeName, IndexError)

  def __getSectionOrRaise__(self, attributeName, exceptionType):
    if self.parser.has_section(attributeName):
      return ConfigSection(attributeName, self.parser)
    raise exceptionType('No section named [%s]', attributeName)

class ConfigSection:
  def __init__(self, name, parser):
    self.sectionName = name
    self.parser = parser

  def getChildren(self):
    out = {}
    for option in self.parser.options(self.sectionName):
      out[option] = self.parser.get(self.sectionName, option)

    return out

  def __getitem__(self, attributeName):
    return self.__getValueOrRaise__(attributeName, IndexError)

  def __getattr__(self, attributeName):
    return self.__getValueOrRaise__(attributeName, AttributeError)

  def __getValueOrRaise__(self, attributeName, exceptionType):
    if self.parser.has_option(self.sectionName, attributeName):
      return self.parser.get(self.sectionName, attributeName)
    raise exceptionType('No option named [%s]', attributeName)

