from formats.yaml.yamlFixture import YamlFixture
from testHelpers import uniqStr

class WhenGettingChildren(YamlFixture):
  def configSetup(self, content):
    self.config = self.loadConfigWithContent(content)

  def setup_method(self, method):
    super(WhenGettingChildren, self).setup_method(method)
    self.element = uniqStr()
    self.configSetup('top: %s' % self.element)

  def testThatGettingChildrenOfConfigReturnsTopLevelElement(self):
    children = self.config.getChildren()
    assert len(children) == 1
    assert children == {'top': self.element}

  def testThatGettingChildrenOfConfigSectionReturnsChildren(self):
    self.configSetup('''
      top:
        element: %s''' % self.element)
    children = self.config.top.getChildren()
    assert len(children) == 1
    assert children == {'element': self.element}

