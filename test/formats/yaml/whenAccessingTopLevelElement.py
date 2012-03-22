from formats.yaml.yamlFixture import YamlFixture
from testHelpers import uniqStr

class WhenAccessingTopLevelElement(YamlFixture):
  def setup_method(self, method):
    super(WhenAccessingTopLevelElement, self).setup_method(method)
    self.elementName = uniqStr()
    self.config = self.loadConfigWithContent('%s: ' % self.elementName)

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

  def testThatDataIsReturnedIfElementHasNoAttributesOrChildren(self):
    expected = uniqStr()
    self.config = self.loadConfigWithContent('top: %s' % expected)
    assert self.config.top == expected

