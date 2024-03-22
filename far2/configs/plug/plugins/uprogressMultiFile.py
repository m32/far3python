import time
import threading
import logging
from far2l.plugin import PluginBase
from far2l.farprogress import ProgressDialog, ProgressState


log = logging.getLogger(__name__)


class Worker(threading.Thread):
    def __init__(self):
        self.state = None

    def run(self):

class Plugin(PluginBase):
    label = "Python Progress MultiFile"
    openFrom = ["PLUGINSMENU"]

    def OpenPlugin(self, OpenFrom):
        tproc = Worker()
        st = ProgressState(tproc, totalsize, countsize)
        t = ProgressMessage(self, "Progress demo", "Please wait ... working", 100)
        t.show()
        time.sleep(2)
        for i in range(0, 100, 20):
            if t.aborted():
                break
            t.update(i)
            time.sleep(2)
        t.close()
