from Character import Character
from Inventory import Inventory
from Item import Item

class Hero:

    def __init__(self, first_name, last_name, race):

        self.character = Character(first_name, last_name, race)
        self.inventory = Inventory()
        self.experience = 25
        self.level = 1

    def get_items(self):

        return self.inventory.items

    def pick_an_item(self, item):

        self.inventory.items.append(item)

    def remove_item(self, item):

        self.inventory.items.remove(item)

hero_1 = Hero("Valentyn", "Potapov", "white")

print(hero_1.character)
hero_1.pick_an_item(Item("ffff", "good", "100"))

for item in hero_1.get_items():
    print(item.name)


