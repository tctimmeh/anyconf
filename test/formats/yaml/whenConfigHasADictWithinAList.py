from formats.yaml.yamlFixture import YamlFixture
from testHelpers import uniqStr

class WhenConfigHasADictWithinAList(YamlFixture):
  def configSetup(self, content):
    self.config = self.loadConfigWithContent(content)

  def setup_method(self, method):
    super(WhenConfigHasADictWithinAList, self).setup_method(method)
    self.element = uniqStr()
    yamlString = '''
                 top:
                   - second: %s
                 ''' % self.element
    self.configSetup(yamlString)

  def testThatAccessingDictInsideListReturnsValue(self):
    assert self.config.top[0].second == self.element

  def testThatCallingGetChildrenReturnsDict(self):
    assert self.config.top[0].getChildren() == {'second': self.element}

