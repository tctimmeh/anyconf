from ...formats import FORMAT_YAML
from ...config import Config

class YamlConfig(Config):
  def __init__(self):
    super(YamlConfig, self).__init__(FORMAT_YAML)