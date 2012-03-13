from anyconf.configFactory import ConfigFactory
from anyconf.formats import FORMAT_INI, FORMAT_YAML, FORMAT_XML
from anyconf.formats.ini.iniConfig import IniConfig
from anyconf.formats.xml.xmlConfig import XmlConfig
from anyconf.formats.yaml.yamlConfig import YamlConfig

class whenGettingConfigFromConfigFactory:

  def testThatConfigFactoryReturnsIniConfigForIniFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_INI)
    assert isinstance(obj, IniConfig)

  def testThatConfigFactoryReturnsIniConfigForIniFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_XML)
    assert isinstance(obj, XmlConfig)

  def testThatConfigFactoryReturnsYamlConfigForYamlFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_YAML)
    assert isinstance(obj, YamlConfig)

  def testThatAnUnknownFormatReturnsNone(self):
    # Wouldn't it make more sense to throw an exception instead?  Like an unsupported format or unknown format exception?
    FORMAT_NOTHING = 0
    obj = ConfigFactory().getConfig(FORMAT_NOTHING)
    assert obj == None


