from .formats.ini.iniConfig import IniConfig
from .formats.xml.xmlConfig import XmlConfig
from .formats.yaml.yamlConfig import YamlConfig
from .formats import FORMAT_INI, FORMAT_XML, FORMAT_YAML

class ConfigLoader:
  def load(self, inputData, dataFormat = None):
    if dataFormat == FORMAT_INI:
      config = IniConfig()
      config.loadFromFile(inputData)
      return config
    elif dataFormat == FORMAT_XML:
      config = XmlConfig()
      config.loadFromFile(inputData)
      return config
    elif dataFormat == FORMAT_YAML:
      config = YamlConfig()
      config.loadFromFile(inputData)
      return config

    return None
