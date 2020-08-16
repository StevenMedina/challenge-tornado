import os

import tornado.ioloop
import tornado.web

from app.main_handler import MainHandler
from app.views.loan_aplication import LoanAplicationHandler


class Routing:
    def _initial_app(self):
        return tornado.web.Application([
            (r"/", MainHandler),
            (r"/loan-application/", LoanAplicationHandler),
        ], static_path=os.path.join(os.path.dirname(__file__), '../static'))
