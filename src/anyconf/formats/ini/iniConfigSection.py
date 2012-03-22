from ...configSection import ConfigSection

class IniConfigSection(ConfigSection):
  def __init__(self, name, sectionName, parser):
    self.name = name
    self.parser = parser
    self.sectionName = sectionName

  def getChildren(self):
    out = self.__getOptions()
    childrenSections = self.__getChildSections()
    out.update(childrenSections)

    return out

  def _getChild(self, name):
    childSectionName = '%s.%s' % (self.name, name)

    child = self._getChildSection(childSectionName)
    if child is not None:
      return child

    return self.__getOptionValue(name)

  def _getChildSection(self, sectionName):
    if self.parser.has_section(sectionName):
      return IniConfigSection(sectionName, sectionName, self.parser)

    for section in self.parser.sections():
      if section.startswith("%s." % sectionName):
        return IniConfigSection(sectionName, None, self.parser)

    return None

  def __getOptionValue(self, name):
    if self.parser.has_option(self.sectionName, name):
      value = self.parser.get(self.sectionName, name)
      return self._decodeOptionValue(value)

  def __getChildSections(self):
    out = {}

    for section in self.parser.sections():
      if not section.startswith("%s." % self.name):
        continue

      childName = self.__getImmediateChildName(section)
      out[childName] = self._getChild(childName)

    return out

  def __getImmediateChildName(self, sectionName):
    nameSizeWithDot = len(self.name) + 1
    childName = sectionName[nameSizeWithDot:].split('.')[0]
    return childName

  def __getOptions(self):
    if self.sectionName is None:
      return {}

    out = {}
    for option in self.parser.options(self.sectionName):
      out[option] = self.parser.get(self.sectionName, option)

    return out

