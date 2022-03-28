import signal
import sys
import pickle
from threading import Thread
from time import sleep

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer, formatPrint


class ConstiVorfuehrungDevice(AbstractVirtualCapability):

    def __init__(self, server):
        super().__init__(server)
        self.uri = "ConstiVorfuehrungDevice"
        self.currently_searching = False

    def SpiralFlight(self, params: dict) -> dict:
        formatPrint(self, "Commencing Siral Flight!!")
        self.currently_searching = True
        while self.currently_searching:
            position = self.invoke_sync("SearchGridGetNextPosition", {})
            self.invoke_sync("FlyToPosition", position)
        return {"SuccessBool": True}

    def CancelSpiralFlight(self, params: dict) -> dict:
        formatPrint(self, "Ending SpiralFlight")
        self.currently_searching = False
        return {"SuccessBool": True}

    def loop(self):
        pass


if __name__ == "__main__":
    # Needed for properly closing when process is being stopped with SIGTERM signal
    def handler(signum, frame):
        print("[Main] Received SIGTERM signal")
        listener.kill()
        quit(1)

    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
        listener = ConstiVorfuehrungDevice(server)
        listener.start()
        signal.signal(signal.SIGTERM, handler)
        listener.join()
        # Needed for properly closing, when program is being stopped wit a Keyboard Interrupt
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")
        server.kill()
        listener.kill()


