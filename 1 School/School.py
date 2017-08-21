
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