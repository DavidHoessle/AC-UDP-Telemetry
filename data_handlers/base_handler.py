from queue import Queue
from threading import Thread
from typing import Callable, Dict


class BaseHandler:
    running = False

    def __init__(self) -> None:
        self.queue = Queue()

    def handle(self) -> None:
        raise NotImplementedError()

    def shutdown(self, *args, **kwargs) -> None:
        pass

    def run(self) -> None:
        while self.running:
            data = self.queue.get()
            self.handle(data)
        
        self.shutdown()

    def start(self) -> None:
        self.running = True
        self.thread = Thread(target=self.run, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.running = False
        self.thread.join()
