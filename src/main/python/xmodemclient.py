import threading

from xmodem import XMODEM1k

class Error(Exception):
    """Base class for other exceptions"""
    pass

class XmodemModeError(Error):
    def __init__(self):
        self.message = "Transfer mode not selected"
        super().__init__(self.message)
    
    pass

class XmodemFileError(Error):
    def __init__(self):
        self.message = "File stream error"
        super().__init__(self.message)
    
    pass

class XmodemClient(threading.Thread):
    DOWNLOAD = 0
    UPLOAD = 1
    
    def __init__(self, serialhandler=None, filename=None, callback=None, mode=None):
        threading.Thread.__init__(self)
        self.serialhandle = serialhandler
        self.filename = filename
        self.callback = callback
        self.stream = None
        self.mode = mode
        if XmodemClient.DOWNLOAD == self.mode:
            try:
                self.stream = open(filename, 'wb')
            except IOError as e:
                raise XmodemFileError
        
        if XmodemClient.UPLOAD == self.mode:
            try:
                self.stream = open(filename, 'rb')
            except FileNotFoundError as e:
                raise XmodemFileError
    
    def getc(self, data, timeout=0):
        return self.serialhandle.getc(data, 0)
    
    def putc(self, data, timeout=0):
        return self.serialhandle.putc(data, 0)
    
    def run(self):
        if self.mode is None:
            raise XmodemModeError
        
        if XmodemClient.DOWNLOAD == self.mode and self.stream is not None:
            try:
                self.xmodem = XMODEM1k(self.getc, self.putc)
                self.xmodem.recv(self.stream, 1, 16, 60, 1, 0, self.callback)
            except Exception as e:
                raise e
            finally:
                self.stream.close()
        
        if XmodemClient.UPLOAD == self.mode and self.stream is not None:
            try:
                self.xmodem = XMODEM1k(self.getc, self.putc)
                self.xmodem.send(self.stream, 128, 60, False, self.callback)
            except Exception as e:
                raise e
            finally:
                self.stream.close()
