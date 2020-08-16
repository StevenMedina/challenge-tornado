import os

import tornado.ioloop
import tornado.web

from .main_handler import MainHandler


class FactoryMainHandlerProcess:
    _port = 8888

    def execute(self):
        self._factory_process()

    def _factory_process(self):
        self._listen_app()

        self._start_service()

    def _initial_app(self):
        return tornado.web.Application([
            (r"/", MainHandler),
        ], static_path=os.path.join(os.path.dirname(__file__), 'static'))

    def _listen_app(self):
        app = self._initial_app()
        app.listen(self._port)

    def _start_service(self):
        tornado.ioloop.IOLoop.current().start()
