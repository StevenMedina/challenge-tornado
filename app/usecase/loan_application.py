from app.exceptions import FieldsRequiredException

from .base import BaseUseCase


class LoanAplicationFactory(BaseUseCase):
    required_fields = [
        "tax_id",
        "business_name",
        "requested_amount",
        "owner_social_security_number",
        "owner_name",
        "owner_email",
    ]
    base_amount = 50000

    def __init__(self, data: list):
        self._data = data

    def execute(self):
        self.valid_data()

        result = self._factory_loan_applications()

        return result

    def valid_data(self):
        self._handle_required_fields()

    def _handle_required_fields(self):
        for required_field in self.required_fields:
            if required_field not in self._data:
                raise FieldsRequiredException(f"field {required_field} is required")

    def _factory_loan_applications(self):
        return self._validate_requested_amount()

    def _validate_requested_amount(self):
        requested_amount = int(self._data["requested_amount"])
        return {
            requested_amount > self.base_amount: "Declined",
            requested_amount == self.base_amount: "Undecided",
            requested_amount < self.base_amount: "Approved",
        }[True]

    def _save_loan_application(self):
        pass # TODO: save in database LoanApplication row
