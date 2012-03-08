from io import StringIO
import anyconf

class WhenLoadingAYamlFile:

  def testThatConfigObjectCanBeCreated(self):
    configLoader = anyconf.ConfigLoader()
    fileObj = StringIO('')
    configLoader.load(fileObj, anyconf.FORMAT_YAML)