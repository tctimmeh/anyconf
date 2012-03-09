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
    return self.__getChildElements(name)

  def __getChildElements(self, name):
    children = self.__collectChildElements(name)

    if len(children) == 1:
      return children[0]
    if len(children):
      return children
    return None

  def __collectChildElements(self, name):
    children = []
    for child in self.element.childNodes:
      if isinstance(child, xml.dom.minidom.Element) and (child.nodeName == name):
        children.append(self._formatChildElement(child))
    return children

  def _formatChildElement(self, element):
    if element.hasAttributes() or self.__hasChildElements(element):
      return XmlConfigSection(element)
    return self.__formatElementCData(element)

  def __hasChildElements(self, element):
    for node in element.childNodes:
      if isinstance(node, xml.dom.minidom.Element):
        return True
    return False

  def __formatElementCData(self, element):
    cdata = self.__getElementCData(element)
    return self.__formatCData(cdata)

  def __formatCData(self, cdata):
    if len(cdata) == 0:
      return True
    if cdata.lower() == 'true':
      return True
    if cdata.lower() == 'false':
      return False
    return cdata

  def __getElementCData(self, element):
    cdata = ''
    for node in element.childNodes:
      if isinstance(node, xml.dom.minidom.Text):
        cdata += node.data
    return cdata.strip()

