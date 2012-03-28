from anyconf.configSection import ConfigSection
from .collator import Collator

class OptionCollator(Collator):
  def __init__(self, parser, sectionName):
    super(OptionCollator, self).__init__(parser)
    self.sectionName = sectionName

  def getOptions(self, name):
    name = name.lower()
    return self._getObjects(name)

  def _getObjectForName(self, name):
    raw = self.parser.get(self.sectionName, name)
    return ConfigSection._decodeOptionValue(raw)

  def _getRawDataSet(self):
    return self.parser.options(self.sectionName)
