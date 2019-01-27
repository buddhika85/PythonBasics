class Student:

    # class attribute
    school_name = "Springfield Elementary"

    # constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_Id = student_id


    def __str__(self):
        return "student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name





