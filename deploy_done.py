# This file is example of deploy.py
# The file is executed once on the first request after every restart of IIS application.
# The file output is redirected to log file described in DEPLOG_LOG environment variable.

import sys
import os
import os.path
import shutil
import django

PROJECT_DIR = os.path.dirname(__file__)
os.chdir(PROJECT_DIR)

PIP_EXE = os.path.join(os.path.dirname(sys.executable), 'scripts\\pip.exe')

# update APPDATA env for pip
os.environ['APPDATA'] = os.path.join(PROJECT_DIR, 'python_modules')

# install requirements to local folder
os.system('{0} install --install-option="--prefix={1}\python_modules" --requirement=requirements.txt'.format(PIP_EXE, PROJECT_DIR))

# run manage.py syncdb --noinput
os.system(sys.executable + " manage.py syncdb --noinput")

# run manage.py migrate
os.system(sys.executable + " manage.py migrate")


"""
if not os.path.exists(os.path.join(PROJECT_DIR, 'static', 'admin', 'css', 'base.css')):
    print 'Copying admin media files'
    shutil.copytree(
      os.path.join(os.path.dirname(django.__file__), 'contrib', 'admin', 'media'),
      os.path.join(PROJECT_DIR, 'static', 'admin'))
else:
    print 'Admin media files already copied'
"""
