from ToDoItem import ToDoItem
from ToDoList import ToDoList

def main():

    showMenu = '''
    1. Show all items
    2. Add new item
    3. Mark item
    4. Archive
    0. Exit\n'''
    print(showMenu)
    choice = input("What would you like to do?: ")
    while choice != "0":
        print(showMenu)
        choice = input("What would you like to do?: ")
        
        if choice == "1":
            ToDoList.show_tasks()
        elif choice == "2":
            name = input("Enter the name of item you want to add: ")
            ToDoList.add_item(ToDoItem(name))
        elif choice == "3":
            name = input("Enter the name of item you want to mark: ")
            ToDoList.mark_item(name)
        elif choice == "4":
            ToDoList.archive()



if __name__ == "__main__":
    main()