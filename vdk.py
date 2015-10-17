#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyVDK - VDK file utility for Python.
https://github.com/gcavallo/pyVDK/

Copyright (c) 2015 by Gabriel Cavallo
BSD 3-Clause License http://opensource.org/licenses/BSD-3-Clause
"""

from __future__ import print_function, division, unicode_literals
import os, sys, binascii, time, zlib, struct

_progress = 0

def unpack(filename):
	"""
	Unpack VDK file data.

	Parameters
	----------
	filename : str
		File name of the VDK.
	"""

	vdk = open(filename, "rb")
	root = os.path.splitext(os.path.basename(filename))[0]
	version, _, files, dirs, size, flist = _header(vdk)
	t1 = time.time()

	try:
		reload(sys); sys.setdefaultencoding('utf8') # Python 2.7+
	except (NameError, AttributeError):
		pass # Python 3.4+

	def recursive(vdk, path="."):
		noffset = 1
		while noffset:
			bit, name, usize, zsize, doffset, noffset = \
				struct.unpack("<?128sIIII", vdk.read(145))
			name = name.decode("cp949").rstrip("\0")

			if bit:
				if not os.path.exists(path):
					os.makedirs(path)

				if name not in (".", ".."):
					recursive(vdk, "{0}/{1}".format(path, name))
			else:
				fpath = "{0}/{1}".format(path, name)

				global _progress
				_progress += 1
				print("[{0:.2%}] Extracting: {1} ..." \
					.format(_progress/files, fpath))

				data = vdk.read(zsize)
				_extract(fpath, data)

	global _progress
	_progress = 0
	recursive(vdk, root)
	vdk.close()

	print("\nExtraction complete! ({0}s)\n" \
		.format(round(time.time() - t1, 2)))

def pack(directory):
	"""
	Pack directory to VDK file.

	Parameters
	----------
	d : str
		Directory name to pack.
	"""

	print("Packing is not implemented yet.")

def info(filename):
	"""
	Print VDK file info.

	Parameters
	----------
	filename : str
		File name of the VDK.
	"""

	vdk = open(filename, "rb")
	h = _header(vdk)
	vdk.close()

	print("Version: {0}\nFiles: {1}\nDirs: {2}\nSize: {3}" \
		.format(h[0], h[2], h[3], h[4]))

	if h[0] == "VDISK1.1":
		print("Filelist size: {0}".format(h[5]))

	return h

def _header(vdk):
	h = list(struct.unpack("<8sIIII", vdk.read(24)))
	h[0] = h[0].decode("utf-8")

	if h[0] == "VDISK1.1":
		h.append(struct.unpack("<I", vdk.read(4))[0])
	elif h[0] == "VDISK1.0":
		h.append(None)
	else:
		sys.exit(1)

	return tuple(h)

def _extract(fpath, data):
	f = open(fpath, "wb")
	d = zlib.decompressobj()
	try:
		f.write(d.decompress(data))
		f.write(d.flush())
	except zlib.error:
		f.truncate(0)
		f.seek(0)
		f.write(data)
	f.close()

def _compress():
	pass

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description=__doc__,
		formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("-c", "--compress", type=pack, metavar="DIR",
		help="compress DIR to a VDK file.")
	parser.add_argument("-e", "--extract", type=unpack, metavar="FILE",
		help="extract VDK file.")
	parser.add_argument("-i", "--info", type=info, metavar="FILE",
		help="show VDK file information.")
	args = parser.parse_args()