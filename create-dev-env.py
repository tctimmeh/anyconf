#!/usr/bin/env python
from __future__ import with_statement
import sys, os, optparse, subprocess, tempfile, re
import virtualenv

def getOptions():
  parser = optparse.OptionParser()
  parser.add_option('--env', dest='environmentName', help='Name of the virtual environment directory to create (default = %default)')
  parser.add_option('--python', dest='python', help='python executable for environment (default = %default)')
  parser.set_defaults(environmentName = 'devenv', python = sys.executable)
  (options, args) = parser.parse_args()
  return options

def findPythonVersion(pythonExecutable):
  pythonRunArgs = [pythonExecutable, '--version']
  pythonProcess = subprocess.Popen(pythonRunArgs, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  pythonVersion = pythonProcess.stdout.read()

  versionRx = re.compile(r'''(\d[\d\.a-zA-Z]+)''')
  match = versionRx.search(pythonVersion)
  return match.group(1)

def createVirtualEnv(pythonExecutable, environmentName):
  virtualEnvOptions = ['--distribute', '--no-site-packages']

  (fd, envCreateScriptFileName) = tempfile.mkstemp()
  try:
    with file(envCreateScriptFileName, 'w') as envCreateScript:
      with file('venv-hooks.py', 'r') as hookFile:
        output = virtualenv.create_bootstrap_script(hookFile.read())

      envCreateScript.write(output)
      envCreateScript.flush()

      cmdArgs = [pythonExecutable, envCreateScriptFileName]
      cmdArgs += virtualEnvOptions
      cmdArgs.append(environmentName)
      ret = subprocess.call(cmdArgs)
      if ret:
        sys.exit(ret)
  finally:
    os.unlink(envCreateScriptFileName)

def printCompletionText(environmentName):
  sys.stdout.write() 
  sys.stdout.write("======================================================")
  sys.stdout.write("Virtual development environment is ready!")
  if sys.platform == 'win32':
    sys.stdout.write("-- Activate it using '%s/Scripts/activate.bat'" % environmentName)
    sys.stdout.write("-- When you're done just run '%s/Scripts/deactivate.bat'" % environmentName)
  else:
    sys.stdout.write("-- Activate it using 'source %s/bin/activate'" % environmentName)
    sys.stdout.write("-- When you're done run 'deactivate'")
  sys.stdout.write("======================================================")
  sys.stdout.write() 

if __name__ == '__main__':
  options = getOptions()
  pythonVersion = findPythonVersion(options.python)

  virtualEnvironmentName = "%s-%s" % (options.environmentName, pythonVersion)

  sys.stdout.write('New environment using python version [%s]\n' % pythonVersion)
  sys.stdout.write('Creating new virtual environment at [%s]\n' % virtualEnvironmentName)

  createVirtualEnv(options.python, virtualEnvironmentName)

