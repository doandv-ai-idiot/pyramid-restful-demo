import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

requires_path = os.path.join(here, 'requirements.txt')

requires = []

with open(requires_path) as f:
    requires.append(f.read())

# Setup
setup(name="app",
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = app:main
      [console_scripts]
      initialize_db = app.scripts.initialize_db:main
      """
      )
