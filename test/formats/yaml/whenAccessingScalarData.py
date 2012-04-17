from formats.yaml.yamlFixture import YamlFixture
from testHelpers import uniqStr

class WhenAccessingScalarData(YamlFixture):
  def configSetup(self, content):
    self.config = self.loadConfigWithContent(content)

  def setup_method(self, method):
    super(WhenAccessingScalarData, self).setup_method(method)

  def setupContentWithScalarValue(self, value):
    self.configSetup('top: %s' % value)

  def testThatfalseReturnsFalse(self):
    self.setupContentWithScalarValue('false')
    assert self.config.top == False

  def testThatFalseReturnsFalse(self):
    self.setupContentWithScalarValue('False')
    assert self.config.top == False

  def testThatFALSEReturnsFalse(self):
    self.setupContentWithScalarValue('FALSE')
    assert self.config.top == False

  def testThattrueReturnsTrue(self):
    self.setupContentWithScalarValue('true')
    assert self.config.top == True

  def testThatTrueReturnsTrue(self):
    self.setupContentWithScalarValue('True')
    assert self.config.top == True

  def testThatTRUEReturnsTrue(self):
    self.setupContentWithScalarValue('TRUE')
    assert self.config.top == True

  def testThatNoneReturnsTrue(self):
    self.setupContentWithScalarValue('')
    assert self.config.top == True
