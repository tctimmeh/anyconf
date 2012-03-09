from .formats.ini.iniConfig import IniConfig
from .formats.xml.xmlConfig import XmlConfig
from .formats import FORMAT_INI, FORMAT_XML

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

    return None
