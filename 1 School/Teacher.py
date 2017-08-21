from Student import Student

class Teacher(Student):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.subjects = [] #list of subjects that this teacher is able to teach



    