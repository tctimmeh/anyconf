import collections
import re
from anyconf.configSection import ConfigSection

class OptionCollator(object):
  def __init__(self, parser, sectionName):
    self.parser = parser
    self.sectionName = sectionName

  def getOptions(self, name):
    name = name.lower()

    optionsByNumber = self.__getOptionsByNumber(name)
    if not len(optionsByNumber):
      return None

    out = self.__getOptionsFromNumbers(optionsByNumber)
    if len(out) == 1:
      return out[0]
    return out

  def __getOptionsByNumber(self, name):
    rxNumberedOptions = re.compile('%s.(\d+)$' % name)

    optionsByNumber = collections.defaultdict(set)
    for option in self.parser.options(self.sectionName):
      if option == name:
        optionsByNumber[0].add(option)
        continue

      m = rxNumberedOptions.match(option)
      if m is not None:
        optionNumber = int(m.group(1))
        optionsByNumber[optionNumber].add(option)

    return optionsByNumber

  def __getOptionsFromNumbers(self, optionsByNumber):
    out = []
    for optionNumber in sorted(optionsByNumber.keys()):
      for option in optionsByNumber[optionNumber]:
        out.append(ConfigSection._decodeOptionValue(self.parser.get(self.sectionName, option)))
    return out

