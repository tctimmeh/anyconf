from testHelpers import uniqStr
from formats.xml.xmlFixture import XmlFixture

class WhenAccessingLists(XmlFixture):
  def setup_method(self, method):
    super(WhenAccessingLists, self).setup_method(method)

    self.firstData = uniqStr()
    self.secondData = uniqStr()

  def testThatElementsAppearingMultipleTimesAreAvailableAsList(self):
    self.config = self.loadConfigWithContent(r'''
      <top>
        <child> %s </child>
        <child> %s </child>
      </top>''' % (self.firstData, self.secondData)
    )

    assert isinstance(self.config.top.child, list)
    assert self.config.top.child[0] == self.firstData
    assert self.config.top.child[1] == self.secondData

  def testThatGettingALoneElementAsListReturnsSingleElementList(self):
    self.config = self.loadConfigWithContent(r'''
      <top>
        <child>%s</child>
      </top>
    ''' % self.firstData)
    assert isinstance(self.config.top.getAsList('child'), list)
    assert self.config.top.getAsList('child')[0] == self.firstData

