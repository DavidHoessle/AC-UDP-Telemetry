class HandlerManager:
    def __init__(self, handlers=None) -> None:
        self.handers = [] if not handlers else handlers

    def register_handler(self, handler):
        self.handlers.append(handler)

    def start_handlers(self):
        for handler in self.handlers:
            handler.start()

    def publish_data(self, data):
        for handler in self.handlers:
            handler.queue.push(data)

    def stop_handlers(self):
        for handler in self.handlers:
            handler.stop()

    def __enter__(self):
        self.start_handlers()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop_handlers()
