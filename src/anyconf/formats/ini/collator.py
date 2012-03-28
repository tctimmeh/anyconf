import collections
import re

class Collator(object):
  def __init__(self, parser):
    self.parser = parser

  def _getObjectForName(self, name):
    pass

  def _getRawDataSet(self):
    pass

  def _getObjects(self, name):
    objectsByNumber = self._getObjectsByNumber(name)
    if not len(objectsByNumber):
      return None
    out = self._getObjectsFromNumbers(objectsByNumber)
    if len(out) == 1:
      return out[0]
    return out

  def _getObjectsByNumber(self, name):
    rxListFormat = re.compile('%s.(\d+)$' % name)

    objectsByNumber = collections.defaultdict(set)
    for configObject in self._getRawDataSet():
      if configObject == name:
        objectsByNumber[0].add(configObject)
        continue

      m = rxListFormat.match(configObject)
      if m is not None:
        objectNumber = int(m.group(1))
        objectsByNumber[objectNumber].add(configObject)

    return objectsByNumber

  def _getObjectsFromNumbers(self, namesByNumber):
    out = []
    for number in sorted(namesByNumber.keys()):
      for name in namesByNumber[number]:
        out.append(self._getObjectForName(name))
    return out

