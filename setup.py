import os
import sys, os.path, platform, warnings

from distutils import log
from distutils.core import setup, Command

VERSION = "0.0.1"

if "GITHUB_RUN_ID" in os.environ:
  VERSION += "." + os.environ["GITHUB_RUN_ID"]

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = None

cmdclass = {
}
if bdist_wheel:
    cmdclass['bdist_wheel'] = bdist_wheel

setup(
  name = "pyyaml-srcinfo-loader",
  version=VERSION,
  packages=['yaml_srcinfo_loader'],
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("Provides a loader for PyYAML that annotates source info on returned elements"),
  license = "Apache 2.0",
  keywords = ["PyYAML"],
  url = "https://github.com/mballance/pyyaml-srcinfo-loader",
  setup_requires=[
    'setuptools_scm',
  ],
  cmdclass=cmdclass,
  install_requires=[
    'pyyaml',
  ],
)

