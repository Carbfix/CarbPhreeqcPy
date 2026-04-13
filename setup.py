#!/usr/bin/python
from pathlib import Path

from setuptools import Distribution, setup

ROOT = Path(__file__).resolve().parent
VERSION_NS = {}
exec((ROOT / "src" / "CarbPhreeqcPy" / "CarbPhreeqcPy.py").read_text(encoding="utf-8"), VERSION_NS)


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(
    name="CarbPhreeqcPy",
    version=VERSION_NS["__version__"],
    author="Martin Voigt",
    download_url="https://github.com/CarbFix/CarbPhreeqcPy",
    license="LGPL V3",
    description="Python wrapper for Iphreeqc",
    long_description=(ROOT / "README.rst").read_text(encoding="utf-8"),
    package_dir={"": "src"},
    packages=["CarbPhreeqcPy"],
    include_package_data=True,
    package_data={
        "CarbPhreeqcPy": [
            "databases/*.dat",
            "libs/*.so*",
            "libs/*.dll",
        ]
    },
    platforms=["Windows", "Linux"],
    distclass=BinaryDistribution,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
