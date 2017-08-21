class Character:

    def __init__(self, first_name, last_name, race):
        self.first_name = first_name
        self.last_name = last_name
        self.race = race

    def __str__(self):
        return self.first_name + self.last_name + self.race

    