#!/usr/bin/python
from pathlib import Path

from setuptools import Distribution, setup

try:
    from setuptools.command.bdist_wheel import bdist_wheel
except ImportError:  # setuptools < 70.1
    from wheel.bdist_wheel import bdist_wheel

ROOT = Path(__file__).resolve().parent
VERSION_NS = {}
exec((ROOT / "src" / "CarbPhreeqcPy" / "CarbPhreeqcPy.py").read_text(encoding="utf-8"), VERSION_NS)


class BinaryDistribution(Distribution):
    # Installs the package into platlib (wheel root), where the bundled
    # ctypes-loaded libraries belong. Without this the payload is diverted
    # into a .data/purelib/ subdirectory.
    def has_ext_modules(self):
        return True


class PlatformWheel(bdist_wheel):
    """Tag the wheel py3-none-<platform>.

    The package is pure Python (no compiled extension module), so it must not
    carry a CPython ABI tag like cp312-cp312 — that makes installation fail
    whenever the target interpreter version differs from the build one
    (has_ext_modules alone would produce that pin; this override removes it).
    It does bundle platform-specific shared libraries loaded via ctypes, so it
    needs a real platform tag — never py3-none-any.

    Build the Linux wheel with:
        python -m build --wheel -C--build-option=--plat-name=manylinux_2_17_x86_64
    """

    def get_tag(self):
        _, _, plat = super().get_tag()
        if plat in ("manylinux_2_17_x86_64", "manylinux2014_x86_64"):
            # Compressed tag set: manylinux2014 is the legacy alias of
            # manylinux_2_17; carrying both keeps the wheel installable
            # regardless of which spelling the installer recognises.
            plat = "manylinux2014_x86_64.manylinux_2_17_x86_64"
        return "py3", "none", plat


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
    include_package_data=False,
    package_data={
        "CarbPhreeqcPy": [
            "databases/*.dat",
            "libs/*.so*",
            "libs/*.dll",
            "*.so*",
            "*.dll",
        ]
    },
    platforms=["Windows", "Linux"],
    distclass=BinaryDistribution,
    cmdclass={"bdist_wheel": PlatformWheel},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
