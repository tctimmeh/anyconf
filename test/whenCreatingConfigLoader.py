import anyconf

class WhenCreatingConfigLoader:
  def testThatTheObjectCreatesWithoutError(self):
    obj = anyconf.ConfigLoader()

