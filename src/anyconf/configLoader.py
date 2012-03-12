from .formats.ini.iniConfig import IniConfig
from .formats.xml.xmlConfig import XmlConfig
from .formats.yaml.yamlConfig import YamlConfig
from .formats import FORMAT_INI, FORMAT_XML, FORMAT_YAML

class ConfigLoader:
  def load(self, inputData, dataFormat = None):
    config = self.createConfig(dataFormat)
    if config:
      config.loadFromFile(inputData)
    return config

  def createConfig(self, dataFormat):
    configOptions = { FORMAT_INI: IniConfig(),
                      FORMAT_XML: XmlConfig(),
                      FORMAT_YAML: YamlConfig()}
    try:
      config = configOptions[dataFormat]
    except KeyError:
      config = None
    return config

