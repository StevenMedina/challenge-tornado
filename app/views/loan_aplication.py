import json

import tornado.web

from app import exceptions
from app.usecase.loan_application import LoanAplicationFactory


class LoanAplicationHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")

    def post(self):
        message = self._run_use_case(data=tornado.escape.json_decode(self.request.body))
        self.write(message)

    def _run_use_case(self, data: list) -> None:
        usecase = LoanAplicationFactory(data=data)
        try:
            result = usecase.execute()
        except exceptions.FieldsRequiredException as err:
            return json.dumps({"status": "error", "message": str(err)})

        return json.dumps({"status": "success", "message": result})


