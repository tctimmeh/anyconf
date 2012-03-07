from io import StringIO
import anyconf

try:
  from ConfigParser import ConfigParser
except ImportError as e:
  from configparser import ConfigParser

class WhenLoadingAYamlFile:

  def testThatConfigObjectCanBeCreated(self):
    configLoader = anyconf.ConfigLoader()
    fileObj = StringIO('')
    configLoader.load(fileObj, anyconf.FORMAT_YAML)