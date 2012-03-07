from ...formats import FORMAT_YAML
from ...config import Config

try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

class YamlConfig(Config):
  def __init__(self):
    super(YamlConfig, self).__init__(FORMAT_YAML)