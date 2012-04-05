from testHelpers import uniqStr
from formats.yaml.yamlFixture import YamlFixture

class WhenAccessingChildEntries(YamlFixture):
  def setup_method(self, method):
    super(WhenAccessingChildEntries, self).setup_method(method)
    self.entryName = uniqStr()
    self.config = self.loadConfigWithContent('''
                                             top:
                                               %s:
                                             ''' % self.entryName)

  def testThatChildIsPropertyOfParent(self):
    assert hasattr(self.config.top, self.entryName)

  def testThatChildIsIndexOfParent(self):
    assert self.config.top[self.entryName] is not None

  def testThatInvalidNameIsNotPropertyOfParent(self):
    assert not hasattr(self.config.top, uniqStr())

  def testThatParentContainsChild(self):
    assert self.entryName in self.config.top

  def testThatThirdLevelChildIsPropertyOfParent(self):
    yamlString = '''
                 top:
                   second:
                     %s:
                 ''' % self.entryName
    config = self.loadConfigWithContent(yamlString)
    assert hasattr(config.top.second, self.entryName)
