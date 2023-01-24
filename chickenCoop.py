class Chicken:

    total_eggs = 0

    def __init__(self, species, name, eggs=0):
        self.species = species
        self.name = name
        self.eggs = eggs

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs