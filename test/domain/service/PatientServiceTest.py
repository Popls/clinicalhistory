import json
import unittest

from domain.model.Patient import Patient
from domain.service.PatientService import PatientService


class MyTestCase(unittest.TestCase):
    patient_service = PatientService()

    def test_patient_is_valid(self):
        with open('../../resource/adult_patient.json') as json_file:
            data = json.load(json_file)
            patient = Patient(data)
            self.assertTrue(self.patient_service.is_valid(patient))

    def test_patient_age_is_not_valid(self):
        with open('../../resource/not_adult_patient.json') as json_file:
            data = json.load(json_file)
            patient = Patient(data)
            self.assertFalse(self.patient_service.is_valid(patient))


if __name__ == '__main__':
    unittest.main()
