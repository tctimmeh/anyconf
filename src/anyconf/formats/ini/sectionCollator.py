import collections
import re
from .iniConfigSection import IniConfigSection

class SectionCollator(object):
  def __init__(self, parser):
    self.parser = parser

  def getSections(self, sectionName):
    baseSection = self.__getConfigSection(sectionName)
    if baseSection is None:
      return None

    sectionsByNumber = self.__getSectionsByNumber(sectionName)
    if not len(sectionsByNumber):
      return baseSection

    out = self.__getSectionsFromNumbers(sectionsByNumber)
    if len(out) == 1:
      return out[0]
    return out

  def __getConfigSection(self, sectionName):
    if self.parser.has_section(sectionName):
      return IniConfigSection(sectionName, sectionName, self.parser)

    for section in self.parser.sections():
      if section.startswith("%s." % sectionName):
        return IniConfigSection(sectionName, None, self.parser)

    return None

  def __getSectionsByNumber(self, sectionName):
    rxNumberedSections = re.compile('%s.(\d+)$' % sectionName)

    siblingsByNumber = collections.defaultdict(set)
    for section in self.parser.sections():
      if section == sectionName:
        siblingsByNumber[0].add(section)
        continue

      match = rxNumberedSections.match(section)
      if match is not None:
        sectionNumber = int(match.group(1))
        siblingsByNumber[sectionNumber].add(section)

    return siblingsByNumber

  def __getSectionsFromNumbers(self, sectionsByNumber):
    out = []
    for sectionNumber in sorted(sectionsByNumber.keys()):
      for section in sectionsByNumber[sectionNumber]:
        out.append(self.__getConfigSection(section))
    return out

