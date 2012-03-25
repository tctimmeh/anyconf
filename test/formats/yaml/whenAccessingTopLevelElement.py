from formats.yaml.yamlFixture import YamlFixture
from testHelpers import uniqStr

class WhenAccessingTopLevelElement(YamlFixture):
  def configSetup(self, content):
    self.config = self.loadConfigWithContent(content)

  def setup_method(self, method):
    super(WhenAccessingTopLevelElement, self).setup_method(method)
    self.elementName = uniqStr()
    self.configSetup('%s: ' % self.elementName)

  def testThatTopLevelElementIsPropertyOfConfig(self):
    assert hasattr(self.config, self.elementName)

  def testThatTopLevelElementIsIndexOfConfig(self):
    assert self.config[self.elementName] is not None

  def testThatConfigContainsTopLevelItem(self):
    assert self.elementName in self.config

  def testThatConfigDoesNotContainItemsThatAreNotTopLevelItems(self):
    assert uniqStr() not in self.config

  def testThatConfigDoesNotHavePropertyForWrongTopLevelItem(self):
    assert not hasattr(self.config, uniqStr())

  def testThatDataIsReturnedIfElementHasNoChildren(self):
    expected = uniqStr()
    self.configSetup('top: %s' % expected)
    assert self.config.top == expected

  def testThatNewlinesArePreservedWhenUsingLiteralStyleBlockForm(self):
    firstString = uniqStr()
    secondString = uniqStr()
    expected = "%s\n%s\n" % (firstString, secondString)
    content = """
      top: |
        %s
        %s
      """ % (firstString, secondString)
    self.configSetup(content)
    assert self.config.top == expected

  def testThatLineBreaksAreFoldedToASpaceWithFoldedStyle(self):
    firstString = uniqStr()
    secondString = uniqStr()
    expected = "%s %s" % (firstString, secondString)
    content = """
      top:
        %s
        %s
      """ % (firstString, secondString)
    self.configSetup(content)
    assert self.config.top == expected

