from __future__ import unicode_literals

from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenAccessingCData(XmlFixture):
  def setup_method(self, method):
    super(WhenAccessingCData, self).setup_method(method)

    self.data = uniqStr()
    self.config = self.loadConfigWithContent('<top><next>%s</next></top>' % self.data)

  def testThatElementDataIsReturned(self):
    assert self.config.top.next == self.data

  def testThatTrueStringsAreBooleanTrue(self):
    self.config = self.loadConfigWithContent('<top><next>true</next></top>')
    assert self.config.top.next == True

  def testThatUppercaseTrueStringsAreBooleanTrue(self):
    self.config = self.loadConfigWithContent('<top><next>TRUE</next></top>')
    assert self.config.top.next == True

  def testThatFalseStringsAreBooleanFalse(self):
    self.config = self.loadConfigWithContent('<top><next>false</next></top>')
    assert self.config.top.next == False

  def testThatUppercaseTrueStringsAreBooleanTrue(self):
    self.config = self.loadConfigWithContent('<top><next>FALSE</next></top>')
    assert self.config.top.next == False


