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
    out = self.__getConfigSection(sectionName)
    if out is None:
      return None

    numberedSiblings = out.__getNumberedSiblings()
    if len(numberedSiblings) > 1:
      return numberedSiblings

    return out

  def __getConfigSection(self, sectionName):
    if self.parser.has_section(sectionName):
      return IniConfigSection(sectionName, sectionName, self.parser)

    for section in self.parser.sections():
      if section.startswith("%s." % sectionName):
        return IniConfigSection(sectionName, None, self.parser)

    return None

  def __getNumberedSiblingNames(self):
    siblingsByNumber = collections.defaultdict(set)
    for section in self.parser.sections():
      if section == self.name:
        siblingsByNumber[0].add(None)
        continue

      match = self.rxNumberedSiblings.match(section)
      if match is not None:
        siblingsByNumber[int(match.group(1))].add(match.group(1))

    return siblingsByNumber

  def __getNumberedSiblings(self):
    siblings = []
    siblingsByNumber = self.__getNumberedSiblingNames()

    for num in sorted(siblingsByNumber.keys()):
      siblings += self.__getSiblingsWithNumbers(siblingsByNumber[num])

    return siblings

  def __getSiblingsWithNumbers(self, numbers):
    out = []
    for number in numbers:
      out.append(self.__getSiblingWithNumber(number))
    return out

  def __getSiblingWithNumber(self, number):
    if number is None:
      return self
    else:
      return self._getChildSection("%s.%s" % (self.name, number))

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

