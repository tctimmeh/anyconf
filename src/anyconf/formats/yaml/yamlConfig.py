from anyconf.formats.yaml.yamlConfigSection import YamlConfigSection
from ...formats import FORMAT_YAML
from ...config import Config

import yaml

class YamlConfig(Config, YamlConfigSection):
  def __init__(self):
    super(YamlConfig, self).__init__(FORMAT_YAML)

  def loadFromFile(self, inputFile):
    self.parser = yaml.load(inputFile)

  def _getChild(self, name):
    try:
      return self._yamlEntryToConfigEntry(self.parser[name])
    except KeyError:
      return None

  def getChildren(self):
    return list(self.parser.keys())
