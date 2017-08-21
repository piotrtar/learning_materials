class ToDoItem:
    
    def __init__(self, name):
        self.name = name
        self.is_marked = False

    def mark(self):
        self.is_marked = True

