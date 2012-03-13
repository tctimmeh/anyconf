from anyconf.configFactory import ConfigFactory

class ConfigLoader:
  def load(self, inputData, dataFormat = None):
    config = ConfigFactory().getConfig(dataFormat)
    if config:
      config.loadFromFile(inputData)
    return config


