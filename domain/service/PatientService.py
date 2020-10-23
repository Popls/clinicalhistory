from domain.model.Patient import Patient
from domain.validator.AgeValidator import AgeValidator
from domain.validator.Validator import Validator


class PatientService:

    def __init__(self):
        self.validator = AgeValidator(Validator())

    def is_valid(self, patient: Patient):
        return self.validator.validate(patient)

