from Class import Class
from Student import Student
from Teacher import Teacher
class School:

    def __init__(self, name):
        self.name = name
        self.classes = []

    def get_best_class(self):
        max_avg_grade_class = 0
        max_avg_grade_class_object = ""
        
        for one_class in self.classes:
            if one_class.get_average_grade() > max_avg_grade_class:
                max_avg_grade_class = one_class.get_average_grade()
                max_avg_grade_class_object = one_class
                
        return max_avg_grade_class_object

    def get_all_teachers(self):
        all_teachers = []

        for one_class in self.classes:
            all_teachers.extend(one_class.teachers)

        return all_teachers

    


class1 = Class("1C")

student1 = Student("Marcin", "Solak")
student1.grades = [4, 5, 2, 3]

student2 = Student("Tomek", "Pipka")
student2.grades = [4, 3, 3, 2]

student3 = Student("Marek", "Cyc")
student3.grades = [4, 3, 5, 6]

teacher1 = Teacher("Brigia", "Wonsz")
teacher2 = Teacher("Maria", "Wrona")

teacher1.subjects = ["Polski", "WOS"]
teacher2.subjects = ["Matma", "Fiza", "Infa"]

class1.students = [student1, student2, student3]
class1.teachers = [teacher1, teacher2]

################################################33

class2 = Class("1B")

student4 = Student("Przemek", "Sołtys")
student4.grades = [3, 2, 4, 4]

student5 = Student("Iza", "Kopara")
student5.grades = [2, 1, 3, 4]

student6 = Student("Ethan", "Carter")
student6.grades = [4, 3, 2, 6]

teacher3 = Teacher("Adam", "Nawałka")
teacher4 = Teacher("Mariusz", "Bielec")

teacher3.subjects = ["Angielski", "Niemiecki"]
teacher4.subjects = ["Przyrka", "Religia", "WF"]

class2.students = [student4, student5, student6]
class2.teachers = [teacher3, teacher4]

#########################################

school = School("Gimba")

school.classes  = [class1, class2]

best_class = school.get_best_class()
print(best_class.name)

all_teachers = school.get_all_teachers()

for teacher in all_teachers:
    print(teacher.get_full_name())