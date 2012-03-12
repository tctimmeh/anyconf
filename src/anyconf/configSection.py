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

  def getAsList(self, attributeName):
    return [self[attributeName]]

  def __getChildOrRaise(self, name, exceptionType):
    out = self._getChild(name)
    if out is not None:
      return out
    raise exceptionType('No child named [%s]' % name)

  def _decodeOptionValue(self, value):
    value = value.strip()
    if not len(value):
      return True

    normalizedValue = value.lower()
    if normalizedValue == 'true':
      return True
    if normalizedValue == 'false':
      return False

    return value

