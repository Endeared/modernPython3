class Character:
    
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    
test = Character("Charles", 100, 112)
test2 = Character("Charlie", 72, 14)

print(test.name)
print(test.hp)
print(test.level)