pyVDK
=====

| VDK file utility for Python.
| https://github.com/gcavallo/pyVDK/
|
| Copyright (c) 2015 by Gabriel Cavallo
| BSD 3-Clause License http://opensource.org/licenses/BSD-3-Clause

Usage as a script
-----------------

.. code-block:: none

	vdk.py [-h] [-c DIR] [-e FILE] [-i FILE]


	  -h, --help            show this help message and exit
	  -c, --compress DIR    compress DIR to a VDK file
	  -e, --extract FILE    extract VDK file
	  -i, --info FILE       show VDK file information

Usage as a module
-----------------

.. autofunction:: vdk.info
.. autofunction:: vdk.pack
.. autofunction:: vdk.unpack