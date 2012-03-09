from __future__ import unicode_literals

from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenAccessingChildElements(XmlFixture):
  def setup_method(self, method):
    super(WhenAccessingChildElements, self).setup_method(method)
    self.elementName = uniqStr()
    self.config = self.loadConfigWithContent('<top><%s /></top>' % self.elementName)

  def testThatChildIsPropertyOfParent(self):
    assert hasattr(self.config.top, self.elementName)

  def testThatChildIsIndexOfParent(self):
    assert self.config.top[self.elementName] is not None

  def testThatInvalidNameIsNotPropertyOfParent(self):
    assert not hasattr(self.config.top, uniqStr())

  def testThatParentContainsChild(self):
    assert self.elementName in self.config.top
