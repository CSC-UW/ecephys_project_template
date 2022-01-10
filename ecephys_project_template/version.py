from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ""  # use '' for first of series, number for 1 and above
_version_extra = "dev"
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = ".".join(map(str, _ver))

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering",
]

# Description should be a one-liner:
description = "ecephys_project_template: Put a one-liner description of your code here"
# Long description will go up on the pypi page
long_description = """
ecephys_project_template: Put a longer description of your code here.
"""

NAME = "ecephys_project_template"
MAINTAINER = "Graham Findlay"
MAINTAINER_EMAIL = "gfindlay@wisc.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/CSC-UW/ecephys_project_template"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Graham Findlay"
AUTHOR_EMAIL = "gfindlay@wisc.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {"ecephys_project_template": [pjoin("data", "*")]}
REQUIRES = [
    "ecephys",
    "ecephys_project_manager",
    "black",
    "jupyter",
]
PYTHON_REQUIRES = ">= 3.7"
