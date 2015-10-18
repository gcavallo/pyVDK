
pyVDK
*****

   VDK file utility for Python.
   https://github.com/gcavallo/pyVDK/

   Copyright (c) 2015 by Gabriel Cavallo
   BSD 3-Clause License http://opensource.org/licenses/BSD-3-Clause


Usage as a script
=================

   vdk.py [-h] [-c DIR] [-e FILE] [-i FILE]


     -h, --help            show this help message and exit
     -c, --compress DIR    compress DIR to a VDK file
     -e, --extract FILE    extract VDK file
     -i, --info FILE       show VDK file information


Usage as a module
=================

vdk.info(filename)

   Prints VDK file information.

   Parameters:
      **filename** (*str*) -- name of file to unpack

   Returns:
      (version, _, files, dirs, size, filelist_size)

   Return type:
      (string, int, int, int, int, int)

vdk.pack(directory)

   Packs directory into a VDK file.

   Parameters:
      **directory** (*str*) -- directory name to pack

vdk.unpack(filename)

   Unpacks VDK file to a directory.

   Parameters:
      **filename** (*str*) -- file name of the VDK
