from distutils.core import setup
import py2exe

setup(console=['run_me.py'], py_modules=['config', 'main', 'Report', 'ShReport', 'SiReport', 'SoReport'
, 'SummaryDict'])