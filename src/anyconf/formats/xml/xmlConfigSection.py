import xml
from ...configSection import ConfigSection
from .helpers import elementToConfigItem

class XmlConfigSection(ConfigSection):
  def __init__(self, element):
    super(XmlConfigSection, self).__init__()
    self.element = element

  def getChildren(self):
    children = set()
    for i in range(self.element.attributes.length):
      children.add(self.element.attributes.item(i).name)
    for child in self.element.childNodes:
      if isinstance(child, xml.dom.minidom.Element):
        children.add(child.nodeName)
    return children

  def _getChild(self, name):
    if self.element.hasAttribute(name):
      return self.element.getAttribute(name)
    return self.__getChildElements(name)

  def __getChildElements(self, name):
    children = self.__collectChildElementsWithName(name)

    if len(children) == 1:
      return children[0]
    if len(children):
      return children
    return None

  def __collectChildElementsWithName(self, name):
    children = []
    for child in self.element.childNodes:
      if isinstance(child, xml.dom.minidom.Element) and (child.nodeName == name):
        children.append(elementToConfigItem(child))
    return children


