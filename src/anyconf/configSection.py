class ConfigSection:
  def getChildren(self):
    return {}

  def __getattr__(self, attributeName):
    raise AttributeError('Internal Error')

  def __getitem__(self, attributeName):
    raise AttributeError('Internal Error')

