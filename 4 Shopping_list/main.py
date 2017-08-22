class Item:

    def __init__(self, name, quantity, unit, price_per_unit, categories, is_bought = False):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price_per_unit = price_per_unit
        self.categories = []
        self.is_bought = is_bought


    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.quantity, self.unit, self.price_per_unit, self.is_bought)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_total_price(self):
        return int(self.quantity) * float(self.price_per_unit)


class ShoppingList:

    def __init__(self, name, date, items):
        self.name = name
        self.date = date
        self.items = items


    def get_total_price(self):
        lista_total = []
        for i in self.items:
            lista_total.append(i.get_total_price())
        return sum(lista_total)

    def sort_by(self, attr):
        lista = []
        for i in self.items:
            lista.append([i.name, i.quantity, i.unit, i.price_per_unit])
        if attr == "quantity":
            return sorted(lista, key=lambda finder: finder[1])
        elif attr == "price":
            return sorted(lista, key=lambda finder: finder[3])
        else:
            return sorted(lista, key=lambda finder: finder[0])

    def get_items(self, is_bought):
        bought_list = []
        not_bought_list = []
        for item in self.items:
            if is_bought == True:
                bought_list.append(item)
            else:
                not_bought_list.append(item)
        if is_bought == True:
            return bought_list, "kupione"
        else:
            return not_bought_list, "nie kupione"

a = Item('banany', "2", "kg", "7", "owoce", True)
b = Item('banany', "5", "kg", "5", "owoce", True)
b = Item('banany', "5", "kg", "5", "owoce", False)
print(a.get_total_price())
c = ShoppingList("filipa lista", "dzisiaj", [a,b])
print(c.get_total_price())
print(c.sort_by("price"))
print(c.get_items(True))

# get_items(is_bought) - returns list of bought or not bought items