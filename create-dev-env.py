#!/usr/bin/env python
from __future__ import with_statement
import sys, os, optparse, subprocess, tempfile
import virtualenv

if __name__ == '__main__':
  parser = optparse.OptionParser()
  parser.add_option('--env', dest='environmentName', help='Name of the virtual environment directory to create (default = %default)')
  parser.set_defaults(environmentName = 'devenv')
  (options, args) = parser.parse_args()

  print 'New environment using python version [%s]' % sys.version
  print 'Creating new virtual environment at [%s]' % options.environmentName

  (fd, envCreateScriptFileName) = tempfile.mkstemp()
  try:
    with file(envCreateScriptFileName, 'w') as envCreateScript:
      with file('venv-hooks.py', 'r') as hookFile:
        output = virtualenv.create_bootstrap_script(hookFile.read())

      envCreateScript.write(output)
      envCreateScript.flush()

      cmdArgs = [sys.executable, envCreateScriptFileName, '--distribute', '--no-site-packages', options.environmentName]
      ret = subprocess.call(cmdArgs)
      if ret:
        sys.exit(ret)
  finally:
    os.unlink(envCreateScriptFileName)

  print 
  print "======================================================" 
  print "Virtual development environment is ready!"
  if sys.platform == 'win32':
    print "-- Activate it using '%s/Scripts/activate.bat'" % options.environmentName
    print "-- When you're done just run '%s/Scripts/deactivate.bat'" % options.environmentName
  else:
    print "-- Activate it using 'source %s/bin/activate'" % options.environmentName
    print "-- When you're done just run 'deactivate'"
  print "======================================================" 
  print 
