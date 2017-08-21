from Character import Character
from Inventory import Inventory
from Item import Item
class Hero():

    def __init__(self, firs_name, last_name, race):
        self.character = Character(firs_name, last_name, race)
        self.inventory = Inventory()
        self.experience = 50
        self.level = 1

        def get_items(self):
            items = []
            for item in self.inventory:
                items.append(item)
            return items

        def pick_an_item(self, item):
            self.inventory.add_item(item)

        def drop_item(self, item):
            self.inventory.drop_item(item)