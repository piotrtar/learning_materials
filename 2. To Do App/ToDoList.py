from ToDoItem import ToDoItem

class ToDoList:

    to_do_items = []

    @classmethod
    def show_tasks(cls):
        for item in cls.to_do_items:
            if item.is_marked == True:
                print("[x] {}".format(item.name))
            else:
                print("[ ] {}".format(item.name))
                

    @classmethod
    def add_item(cls, item):
        cls.to_do_items.append(item)
    
    @classmethod
    def archive(cls):
        updated_items = []
        for item in cls.to_do_items:
            if item.is_marked == False:
                updated_items.append(item)
        cls.to_do_items = updated_items

    @classmethod
    def mark_item(cls, name):
        for item in cls.to_do_items:
            if item.name == name:
                item.mark()
    
    