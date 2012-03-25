from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenGettingChildrenWithSectionLists(IniFixture):
  def setup_method(self, method):
    super(WhenGettingChildrenWithSectionLists, self).setup_method(method)

  def testThatChildListIsInResultsFromTopSection(self):
    content = '''
[section.1]
[section.2]
'''
    config = self.loadConfigWithContent(content)
    assert type(config.getChildren()['section']) is list

  def testThatChildListIsInResults(self):
    content = '''
[section]
[section.child.1]
[section.child.2]
'''
    config = self.loadConfigWithContent(content)
    assert type(config.section.getChildren()['child']) is list

