import xml
from ...configSection import ConfigSection

class XmlConfigSection(ConfigSection):
  def __init__(self, element):
    super(XmlConfigSection, self).__init__()
    self.element = element

  def __getattr__(self, item):
    return self.__getChildOrRaise(item, AttributeError)

  def __getitem__(self, item):
    return self.__getChildOrRaise(item, IndexError)

  def __contains__(self, item):
    return self._getChild(item) is not None

  def __getChildOrRaise(self, item, exceptionType):
    out = self._getChild(item)
    if out is not None:
      return out
    raise exceptionType('No child named [%s]' % item)

  def _getChild(self, name):
    if self.element.hasAttribute(name):
      return self.element.getAttribute(name)

    for child in self.element.childNodes:
      if isinstance(child, xml.dom.minidom.Element) and (child.nodeName == name):
        return XmlConfigSection(child)

    return None

