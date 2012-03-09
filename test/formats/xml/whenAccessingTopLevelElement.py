from __future__ import unicode_literals

from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenAccessingTopLevelElement(XmlFixture):
  def setup_method(self, method):
    super(WhenAccessingTopLevelElement, self).setup_method(method)
    self.elementName = uniqStr()
    self.config = self.loadConfigWithContent('<%s />' % self.elementName)

  def testThatTopLevelElementIsPropertyOfConfig(self):
    assert hasattr(self.config, self.elementName)

  def testThatTopLevelElementIsIndexOfConfig(self):
    assert self.config[self.elementName] is not None

  def testThatConfigContainsTopLevelElement(self):
    assert self.elementName in self.config

  def testThatConfigDoesNotContainItemsThatAreNotTopLevelElement(self):
    assert uniqStr() not in self.config

  def testThatConfigDoesNotHavePropertyForWrongTopLevelElement(self):
    assert not hasattr(self.config, uniqStr())

  def testThatCDataIsReturnedIfElementHasNoAttributesOrChildren(self):
    expected = uniqStr()
    self.config = self.loadConfigWithContent('<top>%s</top>' % expected)
    assert self.config.top == expected
