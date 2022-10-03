import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase
from far3 import fardialogbuilder as dlgb

import socket

log = logging.getLogger(__name__)

HOST = '127.0.0.1'
PORT = 5000

class Plugin(PluginBase):
    class PluginInfo:
        name = 'usocket'
        flags = ffic.PF_NONE
        title = "Python usocket"
        author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
        description = title
        pyguid = uuid.UUID('{308868BA-5773-4C89-8142-DF877868E06A}')
        guid = uuid.UUID('{C3EEFD08-147B-4235-9148-EC90F2AC62A2}')
        version = (1, 0, 0, 0, ffic.VS_SPECIAL)

        openFrom = ["PLUGINSMENU", "COMMANDLINE", "EDITOR", "VIEWER"]

    @staticmethod
    def HandleCommandLine(line):
        return line in ('socket',)

    def CommandLine(self, line):
        try:
            self.xCommandLine(line)
        except:
            log.exception('socket')

    def xCommandLine(self, line):
        log.debug('start')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            log.debug('listen')
            s.listen()
            conn, addr = s.accept()
            log.debug('accept: {}'.format(addr))
            with conn:
                while True:
                    data = conn.recv(1024)
                    log.debug('socket: {}'.format(data))
                    if data.decode() == "stop":
                        conn.close()
                        log.debug('done')
                        return
                    conn.sendall(data)
