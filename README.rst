CarbPhreeqcPy
========== 
.. _PhreeqPy: http://www.phreeqpy.com/
.. _IPhreeqc: http://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/
.. _IPhreeqcPy: https://bitbucket.org/raviapatel/iphreeqcpy
.. _bitbucket: https://bitbucket.org/raviapatel/iphreeqcpy
.. _SCK-CEN: http://www.sckcen.be
.. _python: https://www.python.org/

`CarbPhreeqcPy <https://github.com/CarbFix/CarbPhreeqcPy>`_ provides an updated version of the abandoned `IPhreeqcPy`_ package (see below), including more recent `PHREEQC/IPhreeqc <http://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/>`_ versions as well as adding the `carbfix.dat thermodynamic database <https://github.com/CarbFix/carbfix.dat>`_ to the package.

The original `IPhreeqcPy`_  provides a wrapper to communicate with `IPhreeqc`_ in `python`_. 
It is an alternative to `PhreeqPy`_ and is derived from `PhreeqPy`_. 
One of the drawback of `PhreeqPy`_ was that it used pythonic names spaces for
`IPhreeqc`_  function calls which made `PhreeqPy`_ function calls different
from `IPhreeqc`_. Secondly it did not have automated compilation for `Iphreeqc`_  
during installation. As `PhreeqPy`_ is an open source I took further
liberty to address this issue and redistribute it as `IPhreeqcPy`_ to avoid 
conflicts with development of `PhreeqPy`_. Moreover more Iphreeqc function 
calls are included in `IPhreeqcPy`_ e.g. function calls related to dump which
can be of use while restarting simulations.


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
