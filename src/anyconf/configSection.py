class ConfigSection(object):
  def _getChild(self, name):
    return None

  def getChildren(self):
    return {}

  def __getattr__(self, attributeName):
    return self.__getChildOrRaise(attributeName, AttributeError)

  def __getitem__(self, attributeName):
    return self.__getChildOrRaise(attributeName, IndexError)

  def __contains__(self, attributeName):
    return self._getChild(attributeName) is not None

  def __getChildOrRaise(self, name, exceptionType):
    out = self._getChild(name)
    if out is not None:
      return out
    raise exceptionType('No child named [%s]' % name)