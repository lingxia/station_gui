import py2exe
from distutils.core import setup
setup(windows = ["dapenghost.py"],options = { "py2exe":{"includes":["sip"],"dll_excludes":["MSVCP90.dll"]}})