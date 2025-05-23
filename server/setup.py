# setup.py
from setuptools import setup, find_packages

setup(
  name="accent_classifier",
  version="0.1",
  packages=find_packages(where="server/app"),
  package_dir={"": "server/app"},
)
