from ...config import Config
from .xmlConfigSection import XmlConfigSection
from ...formats import FORMAT_XML

import xml

class XmlConfig(Config, XmlConfigSection):
  def __init__(self):
    super(XmlConfig, self).__init__(FORMAT_XML)

  def loadFromFile(self, inputFile):
    self.parser = xml.dom.minidom.parse(inputFile)

  def _getChild(self, name):
    if self.parser.documentElement.nodeName == name:
      return self._formatChildElement(self.parser.documentElement)

    return None

