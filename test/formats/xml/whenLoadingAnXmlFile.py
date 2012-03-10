import xml.dom.minidom
from formats.xml.xmlFixture import XmlFixture

class WhenLoadingAnXmlFile(XmlFixture):
  def testThatConfigObjectHasXmlDocumentInstance(self):
    config = self.loadConfigWithContent('<test />')
    assert isinstance(config.getParser(), xml.dom.minidom.Document)
