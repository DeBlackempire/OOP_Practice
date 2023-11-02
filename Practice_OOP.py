class Fruit:
    def __init__(self):
        self.name = 'Obi'
        self.color = 'green'
        self.ripe = 'True'

nemo = Fruit()
tess = Fruit()
tess.name = 'Boy'
tess.color = 'Black'
tess.ripe = ' False'
print(tess.name, tess.color, tess.ripe)
print(nemo.name, nemo.color, nemo.ripe)

class Dog:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class BullDog:

    def __init__(self):
        self.color = 'Brown'

class GermanShephard:
    def __init__(self):
        self.color = 'Black'

Bingo = BullDog()



def show(self):
    print(f'The name of my pet is {self.name}, she is {self.color}, color and {self.age}, years old.')
def view(self):
    pass

# jerry = pet('mimi', 'Black', '10')
# plain = pet('yoyo', 'White', '12')
# jerry.show()
# plain.show()