from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if self.pesel is None or len(self.pesel) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(self.pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - (checksum % 10)) % 10

        if control_digit != int(self.pesel[10]):
            return False

        return True

    def field_name(self):
        return RegisterFormFields.PESEL