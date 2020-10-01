from domain.model.Patient import Patient


class PatientService:

    # TODO validators must be out of the this class and set it here
    def __init__(self):
        pass

    def is_valid(self, patient: Patient):
        valid = self.__valid_age(patient)
        # TODO rest of conditions
        return valid

    # TODO remove all comments when do the task
    # This is an example of a condition, use it like a template
    # ----------------------------------------------------------
    # Why @staticmethod? Because any variable of this object is used
    # ----------------------------------------------------------
    # Why "__" before name? Because it's private and it is because
    # doesn't have sense alone. This method only have sense be parting
    # of another method
    @staticmethod
    def __valid_age(patient: Patient):
        return 17 < patient.age < 66
