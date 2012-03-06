from ...config import Config
from ...formats import FORMAT_XML

class XmlConfig(Config):
  def __init__(self):
    super(XmlConfig, self).__init__(FORMAT_XML)