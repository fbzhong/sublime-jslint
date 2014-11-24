try:
    import thread
except ImportError:
    import threading
import functools
import time
import sublime


class StatusProcess(object):
    def __init__(self, msg, listener):
        self.msg = msg
        self.listener = listener
        myThread = threading.Thread(target=self.run_thread)
        myThread.start()

    def run_thread(self):
        progress = ""
        while self.listener.is_running:
            if len(progress) >= 10:
                progress = ""
            progress += "."
            sublime.set_timeout(functools.partial(self.listener.update_status, self.msg, progress), 0)
            time.sleep(0.1)