"""
Wrappers for the "CoreWLAN" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
from pyobjc_setup import setup, Extension

VERSION = "6.2b1"

setup(
    name="pyobjc-framework-CoreWLAN",
    description="Wrappers for the framework CoreWLAN on macOS",
    min_os_level="10.6",
    packages=["CoreWLAN"],
    ext_modules=[
        Extension(
            "CoreWLAN._CoreWLAN",
            ["Modules/_CoreWLAN.m"],
            extra_link_args=["-framework", "CoreWLAN"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreWLAN")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options=dict(bdist_wheel=dict(py_limited_api="cp36")),
)
