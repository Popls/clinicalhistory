from domain.model.Patient import Patient
from domain.validator.Validator import Validator


class AgeValidator(Validator):

    def __init__(self, validator: Validator):
        self.validator = validator

    def validate(self, patient: Patient):
        valid = self.validator.validate(patient)
        return valid & (17 < patient.age < 66)
