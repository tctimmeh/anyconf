from ...config import Config
from ...formats import FORMAT_XML
from .helpers import elementToConfigItem

import xml.dom.minidom

class XmlConfig(Config):
  def __init__(self):
    super(XmlConfig, self).__init__(FORMAT_XML)

  def loadFromFile(self, inputFile):
    self.parser = xml.dom.minidom.parse(inputFile)

  def _getChild(self, name):
    if self.parser.documentElement.nodeName == name:
      return elementToConfigItem(self.parser.documentElement)

    return None
