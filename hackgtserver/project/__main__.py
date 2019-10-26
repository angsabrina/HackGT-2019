"""
    This is the main server file.
"""

import asyncio
import time
import signal
import sys

from threading import Thread

from . import server, database

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        while devServer.is_alive():
            devServer.join(1)
    except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
        sys.exit(1)
    
# Let's initialize the rest api, let's use context switching
database.connect()
devServer = Thread(target=server.api.run)
devServer.setDaemon(True)
devServer.start()
original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)
while True:
    time.sleep(1)