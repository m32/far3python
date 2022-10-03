from cffi import FFI

data = open(__file__+'.cffi', 'rt').read()
ffi = FFI()
ffi.cdef(data)
ffic = ffi.dlopen("python39.dll")
