from OOP.student import Student


# subclass
class HighSchoolStudent(Student):
    # class attribute
    school_name = "Springfield High school"

    # override
    def get_school_name(self):
        return "This is a High school student"

    # super class usage
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
