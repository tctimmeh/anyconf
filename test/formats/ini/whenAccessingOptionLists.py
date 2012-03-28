from .iniFixture import IniFixture
from testHelpers import uniqStr

class WhenAccessingOptionsLists(IniFixture):
  def setup_method(self, method):
    super(WhenAccessingOptionsLists, self).setup_method(method)
    self.values = []
    self.optionNumbers = []

  def createContentLine(self, optionNumber, numberPadding = '', value = None):
    if value is None:
      value = 'opt%d-%s' % (optionNumber, uniqStr())
    self.values.append(value)
    return 'option.%s%d = %s\n' % (numberPadding, optionNumber, value)

  def createContentSection(self):
    return '[section]\n'

  def createContentOptions(self, numberPadding = ''):
    content = ''
    for optionNumber in self.optionNumbers:
      content += self.createContentLine(optionNumber, numberPadding)
    return content

  def createContent(self, numberPadding = ''):
    content = self.createContentSection()
    content += self.createContentOptions(numberPadding)
    return content

  def verifyValues(self, config):
    for i in range(len(self.optionNumbers)):
      assert config.section.option[i] == self.values[i]

  def generateConfig(self, numberPadding = ''):
    content = self.createContent(numberPadding)
    config = self.loadConfigWithContent(content)
    return config

  def testThatOptionListsAreOfTypeList(self):
    self.optionNumbers = range(10)
    config = self.generateConfig()
    assert type(config.section.option) is list

  def testThatOptionsAreAvailableAsList(self):
    self.optionNumbers = range(10)
    config = self.generateConfig()
    self.verifyValues(config)

  def testThatOptionsAreAvailableAsListWhenNumbersHaveGaps(self):
    self.optionNumbers = range(3, 30, 3)
    config = self.generateConfig()
    self.verifyValues(config)

  def testThatOptionsAreListedInNumericalOrder(self):
    self.optionNumbers = range(10, 0, -1)
    config = self.generateConfig()
    self.values.reverse()
    self.verifyValues(config)

  def testThatLeadingZeroesAreIgnored(self):
    self.optionNumbers = range(10)
    config = self.generateConfig(numberPadding = '0')
    self.verifyValues(config)

  def testThatOptionsWithSameNumberAllAppearInList(self):
    self.optionNumbers = list(range(3))
    content = self.createContent()
    self.optionNumbers.append(self.optionNumbers[-1])
    content += self.createContentLine(self.optionNumbers[-1], numberPadding='0')
    config = self.loadConfigWithContent(content)

    actualValues = []
    actualValues.append(config.section.option[-1])
    actualValues.append(config.section.option[-2])

    assert self.values[-1] in actualValues
    assert self.values[-2] in actualValues

  def testThatValuesInOptionListsAreTransformed(self):
    self.optionNumbers = list(range(2))
    content = self.createContent()
    self.optionNumbers.append(99)
    content += self.createContentLine(self.optionNumbers[-1], value = 'true')
    config = self.loadConfigWithContent(content)
    assert config.section.option[-1] is True

  def testThatOptionsWithoutNumbersAreGivenIndexEquivalentOfZero(self):
    self.optionNumbers = list(range(3))
    content = self.createContentSection()
    value = uniqStr()
    self.values.append(value)
    content += 'option = %s\n' % value
    content += self.createContentOptions()
    config = self.loadConfigWithContent(content)

    actualValues = []
    actualValues.append(config.section.option[0])
    actualValues.append(config.section.option[1])

    assert self.values[0] in actualValues
    assert self.values[1] in actualValues

