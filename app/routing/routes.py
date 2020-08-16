import os

import tornado.ioloop
import tornado.web

from app.main_handler import MainHandler


class Routing:
    def _initial_app(self):
        return tornado.web.Application([
            (r"/", MainHandler),
        ], static_path=os.path.join(os.path.dirname(__file__), '../static'))
