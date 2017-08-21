from Teacher import Teacher
from Student import Student
class Class:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def get_best_student(self):
        max_avg_grade = 0 
        for students in self.students:
            if student.get_average_grade() > max_avg_grade:
                max_avg_grade = student.get_average_grade()

        return max_avg_grade

    def get_average_grade(self):
        sum_avg_grade_all_students = 0
        students_amount = len(self.students)

        for student in self.students:
            avarage_student_grade = student.get_average_grade()
            sum_avg_grade_all_students += avarage_student_grade
        
        all_students_avg_grade = sum_avg_grade_all_students/students_amount

        return all_students_avg_grade

    def get_class_subjects(self):
        class_subjects = []

        for teacher in self.teachers:
            class_subjects.extend(teacher.subjects)

        return class_subjects

    def sort_students(alpha_or_grades):
        if alpha_or_grades == "alpha":
            for i in range(len(self.students) - 1):
                for k in range(i, len(self.students) - 1):
                    if self.students[k].get_full_name() > self.students[k+1].get_full_name():
                        self.students[k], self.students[k+1] = self.students[k+1], self.students[k]
            return self.students
        else:
            for i in range(len(self.students) - 1):
                for k in range(i, len(self.students) - 1):
                    if self.students[k].get_average_grade() > self.students[k+1].get_average_grade():
                        self.students[k], self.students[k+1] = self.students[k+1], self.students[k]
            return self.students