from anyconf.configSection import ConfigSection

class YamlConfigSection(ConfigSection):

  def __init__(self, entry):
    super(YamlConfigSection, self).__init__()
    self.entry = entry

  def _getChild(self, name):
    try:
      return self._yamlEntryToConfigEntry(self.entry[name])
    except KeyError:
      return None

  def _yamlEntryToConfigEntry(self, entry):
    if self._hasChildren(entry):
      return YamlConfigSection(entry)
    else:
      return self._getScalarValue(entry)

  def _hasChildren(self, entry):
    return type(entry) == dict

  def _getScalarValue(self, entry):
    if entry is None:
      return ''
    else:
      return entry

