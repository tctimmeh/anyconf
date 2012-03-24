from .iniFixture import IniFixture
from testHelpers import uniqStr
import random

class WhenAccessingSectionLists(IniFixture):
  def setup_method(self, method):
    super(WhenAccessingSectionLists, self).setup_method(method)
    self.sectionName = uniqStr()
    self.values = []
    self.sectionNumbers = []

  def createContentLine(self, sectionNumber, numberPadding = ''):
    value = uniqStr()
    self.values.append(value)
    return '[%s.%s%d]\noption = %s\n' % (self.sectionName, numberPadding, sectionNumber, value)

  def generateContent(self, numberPadding = ''):
    content = ''
    for x in self.sectionNumbers:
      content += self.createContentLine(x, numberPadding)
    return content

  def generateConfig(self, numberPadding = ''):
    content = self.generateContent(numberPadding)
    config = self.loadConfigWithContent(content)
    return config

  def verifySectionValues(self, config):
    for x in range(len(self.sectionNumbers)):
      assert config[self.sectionName][x]['option'] == self.values[x]

  def testThatSectionsAreAvailableAsList(self):
    self.sectionNumbers = range(10)
    config = self.generateConfig()
    self.verifySectionValues(config)

  def testThatSectionsAreAvailableAsListWhenNumberHaveGaps(self):
    self.sectionNumbers = range(3, 30, 3)
    config = self.generateConfig()
    self.verifySectionValues(config)

  def testThatSectionsAreListedInNumericalOrder(self):
    self.sectionNumbers = range(10, 0, -1)
    config = self.generateConfig()
    self.values.reverse()
    self.verifySectionValues(config)

  def testThatLeadingZeroesAreIgnored(self):
    self.sectionNumbers = range(10)
    config = self.generateConfig(numberPadding='0')
    self.verifySectionValues(config)

  def testThatSectionsWithSameNumberBothAppearInList(self):
    self.sectionNumbers = list(range(3))
    content = self.generateContent()
    self.sectionNumbers.append(self.sectionNumbers[-1])
    content += self.createContentLine(self.sectionNumbers[-1], numberPadding='0')
    config = self.loadConfigWithContent(content)

    numSections = len(self.sectionNumbers)
    actualValues = []
    actualValues.append(config[self.sectionName][numSections - 2]['option'])
    actualValues.append(config[self.sectionName][numSections - 1]['option'])

    assert self.values[-2] in actualValues
    assert self.values[-1] in actualValues

