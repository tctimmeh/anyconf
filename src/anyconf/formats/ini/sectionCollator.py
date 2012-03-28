from .iniConfigSection import IniConfigSection
from .collator import Collator

class SectionCollator(Collator):
  def __init__(self, parser):
    super(SectionCollator, self).__init__(parser)

  def getSections(self, sectionName):
    section = self._getObjects(sectionName)
    if section is None:
      return self.__getConfigSection(sectionName)
    return section

  def __getConfigSection(self, sectionName):
    if self.parser.has_section(sectionName):
      return IniConfigSection(sectionName, sectionName, self.parser)

    for section in self.parser.sections():
      if section.startswith("%s." % sectionName):
        return IniConfigSection(sectionName, None, self.parser)

    return None

  def _getObjectForName(self, name):
   return self.__getConfigSection(name)

  def _getRawDataSet(self):
    return self.parser.sections()
