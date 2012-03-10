import xml

def elementToConfigItem(element):
  if element.hasAttributes() or hasChildElements(element):
    return XmlConfigSection(element)
  return formatElementCData(element)

def hasChildElements(element):
  for node in element.childNodes:
    if isinstance(node, xml.dom.minidom.Element):
      return True
  return False

def formatElementCData(element):
  cdata = getElementCData(element)
  return parseSpecialCData(cdata)

def parseSpecialCData(cdata):
  if len(cdata) == 0:
    return True
  if cdata.lower() == 'true':
    return True
  if cdata.lower() == 'false':
    return False
  return cdata

def getElementCData(element):
  cdata = ''
  for node in element.childNodes:
    if isinstance(node, xml.dom.minidom.Text):
      cdata += node.data
  return cdata.strip()

from .xmlConfigSection import XmlConfigSection

