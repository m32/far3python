from cffi import FFI

data = open(__file__+'.h', 'rt').read()
ffi = FFI()
ffi.cdef(data)
ffic = ffi.dlopen("python39.dll")
