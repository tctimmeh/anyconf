import string, random

def uniqStr():
  return random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))


