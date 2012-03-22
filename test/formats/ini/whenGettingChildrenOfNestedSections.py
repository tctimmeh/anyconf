from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenGettingChildrenOfNestedSections(IniFixture):
  def setup_method(self, method):
    super(WhenGettingChildrenOfNestedSections, self).setup_method(method)
    self.section1 = 's1' + uniqStr()
    self.section2 = 's2' + uniqStr()
    self.section3 = 's3' + uniqStr().lower()
    self.option = 'opt' + uniqStr().lower()
    self.value = 'val' + uniqStr()

  def section1Name(self):
    return self.section1

  def section2Name(self):
    return '.'.join((self.section1, self.section2))

  def section3Name(self):
    return '.'.join((self.section2Name(), self.section3))

  def testThatChildSectionsAreListed(self):
    config = self.loadConfigWithContent('''
[%s]
    ''' % (
      self.section3Name()
      ))
    children = config[self.section1][self.section2].getChildren()
    assert children[self.section3] is not None

  def testThatChildOptionsAreListed(self):
    config = self.loadConfigWithContent('''
[%s]
%s = %s
    ''' % (
      self.section2Name(),
      self.option, self.value
      ))
    children = config[self.section1][self.section2].getChildren()
    assert children[self.option] == self.value

  def testThatConflictingSectionAndOptionNamesReturnSection(self):
    config = self.loadConfigWithContent('''
[%s]
%s = %s
[%s]
    ''' % (
      self.section2Name(),
      self.section3Name(), self.value,
      self.section3Name()
    ))
    children = config[self.section1][self.section2].getChildren()
    assert children[self.section3] != self.value

  def testThatChildrenOfConfigContainsChildSectionsThatHaveChildren(self):
    config = self.loadConfigWithContent('''
[%s]
%s = %s
[%s]
    ''' % (
      self.section1Name(),
      self.option, self.value,
      self.section2Name()
      ))
    assert config.getChildren()[self.section1][self.option] == self.value

  def testThatChildrenOfSectionsContainChildSectionsThatHaveChildren(self):
    config = self.loadConfigWithContent('''
[%s]
%s = %s
[%s]
    ''' % (
      self.section2Name(),
      self.option, self.value,
      self.section3Name()
      ))
    assert config[self.section1].getChildren()[self.section2][self.option] == self.value

  def testThatChildSectionsOverrideOptionsWithTheSameName(self):
    config = self.loadConfigWithContent('''
[%s]
%s = %s
[%s]
    ''' % (
      self.section1Name(),
      self.option, self.value,
      '.'.join((self.section1Name(), self.option))
      ))
    assert config[self.section1].getChildren()[self.option] != self.value

