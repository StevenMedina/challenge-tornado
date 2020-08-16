import os

import tornado.ioloop
import tornado.web

from app.routing.routes import Routing


class FactoryMainHandlerProcess:
    _port = 8888

    def execute(self):
        self._factory_process()

    def _factory_process(self):
        self._listen_app()

        self._start_service()

    def _initial_app(self):
        routing = Routing()
        return routing._initial_app()

    def _listen_app(self):
        app = self._initial_app()
        app.listen(self._port)

    def _start_service(self):
        tornado.ioloop.IOLoop.current().start()
