from __future__ import unicode_literals

import xml.dom.minidom
from io import StringIO
import anyconf

class WhenLoadingAnIniFile:
  def setup_method(self, method):
    self.configLoader = anyconf.ConfigLoader()

  def loadConfigWithContent(self, content):
    fileObj = StringIO(content)
    return self.configLoader.load(fileObj, anyconf.FORMAT_XML)

  def testThatConfigObjectHasXmlDocumentInstance(self):
    config = self.loadConfigWithContent('<test />')
    assert isinstance(config.getParser(), xml.dom.minidom.Document)
