class Inventory:

    def __init__(self):

        self.capacity = 100
        self.max_weight = 80
        self.items = []

    def add_item(self, item):

        if item.weight < self.max_weight:
            self.items.append(item)

        return self.items

    def drop_item(self, item_name):

        for item in self.items:
            if item == item_name:
                self.items.remove(item)

        return self.items

    def get_inventory_size(self):

        return len(self.items)

    def get_inventory_weight(self):

        return sum(self.items)

    def get_heaviest_item(self):

        return max(self.items)




