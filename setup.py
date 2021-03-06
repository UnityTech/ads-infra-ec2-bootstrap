import sys
import ez_setup

ez_setup.use_setuptools()

from bootstrap import __version__
from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    raise NotImplementedError("python 2.7 or higher required")

setup(
    name='bootstrap',
    version=__version__,
    packages=find_packages()
)
