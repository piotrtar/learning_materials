
class Inventory:

    def __init__(self):
        self.capacity = 40
        self.max_weight = 100
        self.items = []

    def add_item(self, item):
        capacity_sum = sum(self.items)
        weight_sum = 0
        for item in self.items:
            weight_sum += item.weight
        
        weight_after_adding_item = weight_sum + item.weight

        if capacity_sum < self.capacity and weight_after_adding_item < self.max_weight:
            self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_inventory_size(self):
        inventory_size = len(self.items)
        return inventory_size

    def get_inventory_weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        
        return total_weight
    
    def get_the_haviest_item(self):
        haviest_item = self.items[0]

        for item in self.items:
            if item.weight > haviest_item:
                haviest_item = item
        return haviest_item