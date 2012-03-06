from .configSection import ConfigSection

class Config(ConfigSection):
  def __init__(self, fileFormat):
    self.fmt = fileFormat
    self.parser = None

  def loadFromFile(self, inputFile):
    pass

  def getFormat(self):
    return self.fmt

  def getParser(self):
    return self.parser
