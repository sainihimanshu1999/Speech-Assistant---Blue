"""
Wrappers for the "PencilKit" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup
import os

VERSION = "6.2b1"

setup(
    name="pyobjc-framework-PencilKit",
    description="Wrappers for the framework PencilKit on macOS",
    min_os_level="10.15",
    packages=["PencilKit"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
