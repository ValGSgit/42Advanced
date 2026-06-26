# With all metadata living in setup.cfg, setup.py shrinks to this shim.
# (Kept so that older `python setup.py ...` style commands still work.)
from setuptools import setup

setup()
