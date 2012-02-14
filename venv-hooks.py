import sys, os, subprocess

def after_install(options, home_dir):
  if sys.platform == 'win32':
    bin = 'Scripts'
  else:
    bin = 'bin'

  pipPackages = [
    'pytest >= 2.1',
  ]
  easyInstallPackages = [
  ]

  for package in pipPackages:
    subprocess.call([os.path.join(home_dir, bin, 'pip'), 'install', package])
  for package in easyInstallPackages:
    subprocess.call([os.path.join(home_dir, bin, 'easy_install'), package])

  subprocess.call([os.path.join(home_dir, bin, 'python'), './setup.py', 'develop'])

