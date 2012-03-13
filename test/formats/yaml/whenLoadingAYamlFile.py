from formats.yaml.yamlFixture import YamlFixture

class WhenLoadingAYamlFile(YamlFixture):

  def setup_method(self, method):
    super(WhenLoadingAYamlFile, self).setup_method(method)

  def testThatConfigObjectHasDictInstance(self):
    config = self.loadConfigWithContent('test:')
    assert isinstance(config.getParser(), dict)