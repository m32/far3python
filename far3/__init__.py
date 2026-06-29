try:
    import uuid
    from far3.far3cffi import ffi, ffic
    from .pluginmanager import PluginManager

    pluginmanager = PluginManager()
except:
    import traceback
    with open('w:/far3.err.log') as fp:
        traceback.print_exc(file=fp)
