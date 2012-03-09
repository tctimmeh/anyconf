from anyconf.configSection import ConfigSection
from ...config import Config
from ...formats import FORMAT_XML

import xml

class XmlConfig(Config):
  def __init__(self):
    super(XmlConfig, self).__init__(FORMAT_XML)

  def loadFromFile(self, inputFile):
    self.parser = xml.dom.minidom.parse(inputFile)

  def __getattr__(self, attributeName):
    if self.parser.documentElement.nodeName == attributeName:
      return ConfigSection()
    raise AttributeError('Internal Error')

  def __getitem__(self, attributeName):
    if self.parser.documentElement.nodeName == attributeName:
      return ConfigSection()
    raise AttributeError('Internal Error')

  def __contains__(self, attributeName):
    if self.parser.documentElement.nodeName == attributeName:
      return True
    return False
