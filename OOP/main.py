# access class attribute
from OOP.hs_student import HighSchoolStudent
from OOP.student import Student

print(Student.school_name)

# class instantiation
student = Student("Buddhika", 1)
print(student.get_name_capitalize())
print(student.get_school_name())

# sub class
james = HighSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())