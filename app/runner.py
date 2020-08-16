import os

import tornado.ioloop
import tornado.web

from app.routing.routes import Routing
from app.database.orm import ORMManager


class FactoryMainHandlerProcess:
    _port = 8888

    def execute(self):
        self._factory_process()

    def _factory_process(self):
        self._listen_app()

        self._connection = self._execute_statement(
            "create",
            "LoanApplication",
            {
                "id integer PRIMARY KEY": "",
                "tax_id bigint NOT NULL": "",
                "business_name varchar NOT NULL": "",
                "requested_amount text NOT NULL": "",
                "owner_social_security_number smallint NOT NULL": "",
                "owner_name varchar NOT NULL": "",
                "owner_email varchar NOT NULL": "",
                "status varchar NOT NULL": "",
            }
        )

        self._start_service()

    def _execute_statement(self, statement: str, table_name: str, dict_statement: dict):
        orm_manager = ORMManager(
            statement=statement, table_name=table_name, dict_statement=dict_statement
        )
        return orm_manager.execute()

    def _initial_app(self):
        routing = Routing()
        return routing._initial_app()

    def _listen_app(self):
        app = self._initial_app()
        app.listen(self._port)

    def _start_service(self):
        tornado.ioloop.IOLoop.current().start()
