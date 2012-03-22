from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenAccessingNestedSections(IniFixture):
  def setup_method(self, method):
    super(WhenAccessingNestedSections, self).setup_method(method)
    self.section1 = uniqStr()
    self.section2 = uniqStr()
    self.section3 = uniqStr().lower()
    self.config = self.loadConfigWithContent("[%s]" % ('.'.join((self.section1, self.section2, self.section3))))

  def testThatChildSectionsAreContainedByParentSections(self):
    assert self.section3 in self.config[self.section1][self.section2]

  def testThatSubsetsOfSectionNamesAreNotInSection(self):
    assert self.section2[0] not in self.config[self.section1]

