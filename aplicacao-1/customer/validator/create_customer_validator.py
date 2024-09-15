import re
from cerberus.validator import Validator

create_customer_schema = {
    "name": {"type": "string", "required": True, "minlength": 1, "maxlength": 70},
    "email": {
        "type": "string",
        "email": True,
        "required": True,
        "minlength": 1,
        "maxlength": 70,
    },
    "phone": {"type": "string", "required": True, "phonelength": True},
    "age": {"type": "integer", "required": True, "min": 1, "max": 150, "coerce": int},
}


class CustomValidator(Validator):
    def _validate_email(self, constraint, field, value):
        pattern = r"^[\w.+-]+@[\da-zA-Z-]+\.[\da-zA-Z-.]+$"

        regex_found = re.search(pattern=pattern, string=value)
        email_is_wrong = regex_found == None

        validation_is_enabled = constraint is True

        if validation_is_enabled and email_is_wrong:
            self._error(field, "Não está no formato de email.")

    def _validate_phonelength(self, constraint, field, value):
        phone_is_wrong = not (
            len(value) == 8 or len(value) == 9 or len(value) == 11 or len(value) == 13
        )

        validation_is_enabled = constraint is True

        if validation_is_enabled and phone_is_wrong:
            self._error(field, "Deve conter 8, 9, 11 ou 13 números.")


class CreateCustomerValidator:
    def __init__(self) -> None:
        pass

    def execute(self, data: dict):
        v = CustomValidator()
        v.allow_unknown = False
        v.validate(data, create_customer_schema)
        return v.errors
