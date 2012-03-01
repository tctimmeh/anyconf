from .config import Config

class ConfigLoader:
  def load(self, inputData, dataFormat = None):
    return Config(dataFormat)
