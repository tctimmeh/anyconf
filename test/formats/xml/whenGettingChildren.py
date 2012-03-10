from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenGettingChildren(XmlFixture):
  def setup_method(self, method):
    super(WhenGettingChildren, self).setup_method(method)

  def testThatGettingChildrenOfConfigReturnsTopLevelElement(self):
    content = uniqStr()
    self.config = self.loadConfigWithContent('<top>%s</top>' % content)

    children = self.config.getChildren()
    assert len(children) == 1
    assert children[0] == content

  def testThatGettingChildrenReturnsAttributeNames(self):
    content = '<top '
    attributes = []
    for i in range(5):
      attributeName = uniqStr()
      content += '%s="%s" ' % (attributeName, uniqStr())
      attributes.append(attributeName)
    content += ' />'

    self.config = self.loadConfigWithContent(content)
    children = self.config.top.getChildren()

    assert len(children) == len(attributes)
    for attributeName in attributes:
      assert attributeName in children

  def testThatGettingChildrenReturnsChildElementNames(self):
    content = '<top>'
    elements = []
    for i in range(5):
      elementName = uniqStr()
      content += '<%s />' % elementName
      elements.append(elementName)
    content += '</top>'

    self.config = self.loadConfigWithContent(content)
    children = self.config.top.getChildren()

    assert len(children) == len(elements)
    for elementName in elements:
      assert elementName in children

