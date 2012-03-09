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

  def _getChild(self, name):
    if self.parser.has_option(self.sectionName, name):
      return self.parser.get(self.sectionName, name)
    return None

