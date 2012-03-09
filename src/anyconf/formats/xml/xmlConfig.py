from ...config import Config
from ...formats import FORMAT_XML

import xml

class XmlConfig(Config):
  def __init__(self):
    super(XmlConfig, self).__init__(FORMAT_XML)

  def loadFromFile(self, inputFile):
    self.parser = xml.dom.minidom.parse(inputFile)

