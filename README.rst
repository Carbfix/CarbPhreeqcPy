CarbPhreeqcPy
=============
.. _PhreeqPy: http://www.phreeqpy.com/
.. _IPhreeqc: http://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/
.. _IPhreeqcPy: https://bitbucket.org/raviapatel/iphreeqcpy
.. _bitbucket: https://bitbucket.org/raviapatel/iphreeqcpy
.. _SCK-CEN: http://www.sckcen.be
.. _Python: https://www.python.org/

`CarbPhreeqcPy <https://github.com/CarbFix/CarbPhreeqcPy>`_ provides an updated version of the abandoned `IPhreeqcPy`_ package (see below), including more recent `PHREEQC/IPhreeqc <http://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/>`_ versions as well as adding the `carbfix.dat thermodynamic database <https://github.com/CarbFix/carbfix.dat>`_ to the package.

The `IPhreeqcPy`_  provided a wrapper to communicate with `IPhreeqc`_ in `Python`_.
Ravi A. Patel created it as an alternative to `PhreeqPy`_ and is derived from `PhreeqPy`_. 


Building the wheel
++++++++++++++++++

The package is pure Python plus two bundled shared libraries
(``src/CarbPhreeqcPy/libs/IPhreeqc.dll`` for Windows and
``src/CarbPhreeqcPy/libs/libIPhreeqc.so.3.6.3`` for Linux) that are loaded
with ``ctypes`` at runtime. Nothing is compiled during the build, so wheels
for **both** platforms can be built from any machine:

.. code-block:: console

    pip install build

    # Wheel for the platform you are on (e.g. py3-none-win_amd64 on Windows)
    python -m build --wheel

    # Linux/Databricks wheel, buildable from any OS
    python -m build --wheel -C--build-option=--plat-name=manylinux_2_17_x86_64

Both wheels carry the identical payload; only the platform tag in the
filename and ``WHEEL`` metadata differs. Built wheels are committed to
``dist/`` so consuming repos can reference them directly.

Releasing a new version:

1. Bump ``__version__`` in ``src/CarbPhreeqcPy/CarbPhreeqcPy.py`` (the single
   source of truth; ``setup.py`` reads it from there). Every change to the
   package contents needs a new version — one version number must identify
   exactly one build.
2. Build both wheels as above and replace the old ones in ``dist/``.

Wheel tagging — do not change this
++++++++++++++++++++++++++++++++++

Wheels are deliberately tagged ``py3-none-<platform>`` (e.g.
``py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64``), configured in
``setup.py``:

- **No CPython ABI pin** (not ``cp312-cp312``): the package has no compiled
  extension module, so pinning the interpreter version is wrong and made
  installs fail whenever the target interpreter (e.g. on Databricks
  serverless) differed from the build one.
- **Not** ``py3-none-any``: the bundled shared libraries are
  platform-specific, and the platform tag is also what makes installers
  place the package in ``platlib``. A ``py3-none-any`` build previously
  broke library loading — do not reintroduce it.
- The Linux wheel carries both the ``manylinux2014_x86_64`` and
  ``manylinux_2_17_x86_64`` tags because they are aliases and installers
  vary in which spelling they recognise.

Changes when upgrading from 1.0.3
+++++++++++++++++++++++++++++++++

- Version 1.0.3 existed as three different builds with differing contents
  (``cp311-cp311-win_amd64``, ``cp312-cp312-manylinux2014_x86_64`` and
  ``py3-none-any``). All three are retired; do not copy them into new
  projects. 1.0.4 is the first unambiguous version.
- Wheel filenames changed, in two ways: the tag (see above) and the name
  part, which recent setuptools normalises to lowercase
  (``carbphreeqcpy-1.0.4-...`` instead of ``CarbPhreeqcPy-1.0.3-...``).
  Anything that references a wheel by path — ``requirements.txt`` entries,
  Databricks job/cluster library configuration, Terraform variables — must
  be updated to the new filename. ``pip`` itself treats the names
  identically; ``import CarbPhreeqcPy`` and the Python API are unchanged.
- No code or thermodynamic database contents changed between the good 1.0.3
  build and 1.0.4 apart from the version number itself.


Developer
++++++++++
Martin Voigt

`IPhreeqcPy`_: Ravi A. Patel


License and Terms of use
++++++++++++++++++++++++

`CarbPhreecPy <https://github.com/CarbFix/CarbPhreeqcPy>`_ is a free software: you can redistribute it and/or modify it 
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, version 3 of the License. This program is distributed
in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU Lesser General Public License for more details. You should have 
received a copy of the GNU Lesser General Public License along with this program.
If not, see `<http://www.gnu.org/licenses/>`_.
