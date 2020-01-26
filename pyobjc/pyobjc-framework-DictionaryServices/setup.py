"""
Deprecated wrappers for the "DictionaryServices" framework on macOS 10.5 or later.

Use package "CoreServices" instead.
"""
from pyobjc_setup import setup
import os

VERSION = "6.2b1"

setup(
    name="pyobjc-framework-DictionaryServices",
    description="Wrappers for the framework DictionaryServices on macOS",
    min_os_level="10.5",
    packages=["DictionaryServices"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreServices>=" + VERSION,
    ],
    long_description=__doc__,
)
