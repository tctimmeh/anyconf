from ...formats import FORMAT_YAML
from ...config import Config

import yaml

class YamlConfig(Config):
  def __init__(self):
    super(YamlConfig, self).__init__(FORMAT_YAML)

  def loadFromFile(self, inputFile):
    self.parser = yaml.load(inputFile)