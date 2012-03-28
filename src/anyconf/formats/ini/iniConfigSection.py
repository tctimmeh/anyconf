import collections
import re
from anyconf.formats.ini.optionCollator import OptionCollator
from ...configSection import ConfigSection

class IniConfigSection(ConfigSection):
  def __init__(self, name, sectionName, parser):
    self.name = name
    self.parser = parser
    self.sectionName = sectionName
    self.rxNumberedSiblings = re.compile('%s.(\d+)$' % self.name)

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
    collator = SectionCollator(self.parser)
    return collator.getSections(sectionName)

  def __getChildSections(self):
    out = {}

    for section in self.parser.sections():
      if not section.startswith("%s." % self.name):
        continue

      childName = self.__getImmediateChildName(section)
      if childName in out:
        continue
      out[childName] = self._getChild(childName)

    return out

  def __getImmediateChildName(self, sectionName):
    nameSizeWithDot = len(self.name) + 1
    childName = sectionName[nameSizeWithDot:].split('.')[0]
    return childName

  def __getOptionValue(self, name):
    if self.sectionName is None:
      return None
    return OptionCollator(self.parser, self.sectionName).getOptions(name)

  def __getOptions(self):
    if self.sectionName is None:
      return {}

    out = {}
    for option in self.parser.options(self.sectionName):
      out[option] = self.parser.get(self.sectionName, option)

    return out

from anyconf.formats.ini.sectionCollator import SectionCollator

