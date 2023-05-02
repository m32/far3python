#!/usr/bin/env vpython3
import sys
import os
import re
import pcpp
import io
import cffi

far3sdk = sys.argv[1]

cpp = pcpp.Preprocessor()
cpp.add_path(far3sdk)
data = open('far3cffi.h', 'rt').read()
cpp.parse(data)
fp = io.StringIO()
cpp.write(fp)

data = fp.getvalue()
for s in re.findall("'.+'", data):
    t = str(ord(s[-2].encode("ascii")))
    data = data.replace(s, t)
data = data.replace("#line", "//#line")
data = data.replace("#pragma", "//#pragma")
open('far3cffi.py.h', 'wt').write(data)

if 0:
    ffi = cffi.FFI()
    ffi.set_source('far3cffi', None)
    ffi.cdef(data, packed=True)
    #ffi.compile(verbose=True)
    ffi.compile('', libraries=[])
