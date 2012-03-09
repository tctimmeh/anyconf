from __future__ import unicode_literals

from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenAccessingAttributes(XmlFixture):
  def setup_method(self, method):
    super(WhenAccessingAttributes, self).setup_method(method)
    self.attributeName = uniqStr()
    self.attributeValue = uniqStr()
    self.config = self.loadConfigWithContent('<top %s = "%s"/>' % (self.attributeName, self.attributeValue))

  def testThatAttributeIsPropertyOfElement(self):
    assert getattr(self.config.top, self.attributeName) == self.attributeValue

  def testThatAttributeIsIndexOfElement(self):
    assert self.config.top[self.attributeName] == self.attributeValue

  def testThatAttributeValueIsReturnedWhenNameConflictsWithChildElement(self):
    self.config = self.loadConfigWithContent('<top %s = "%s"><%s /></top>' % (self.attributeName, self.attributeValue, self.attributeName))
    assert self.config.top[self.attributeName] == self.attributeValue

  def testThatElementContainsAttribute(self):
    assert self.attributeName in self.config.top
