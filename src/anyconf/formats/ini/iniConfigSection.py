from ...configSection import ConfigSection

class IniConfigSection(ConfigSection):
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
