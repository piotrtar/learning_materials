class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_average_grade(self):
        sum_of_grades = 0
        amount_of_grades = len(self.grades)
        for grade in self.grades:
            sum_of_grades += grade
        
        avarage_grades = sum_of_grades/amount_of_grades
        return avarage_grades

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

