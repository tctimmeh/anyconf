try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

class Config:
  def __init__(self, data, fmt):
    self.fmt = fmt

    self.parser = ConfigParser()
    self.parser.readfp(data)

  def __getattr__(self, attributeName):
    if self.parser.has_section(attributeName):
      return True
    raise AttributeError('No section named [%s]', attributeName)

  def __getitem__(self, attributeName):
    if self.parser.has_section(attributeName):
      return True
    raise IndexError('No section named [%s]', attributeName)

  def getFormat(self):
    return self.fmt

  def getParser(self):
    return self.parser
