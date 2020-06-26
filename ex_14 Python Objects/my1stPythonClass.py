class PartyAnimal:
    x = 0
    name = ''
    # constructor with variab;e
    def __init__(self, z):
        self.name = z
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far', self.x)

    # destructor
    def __del__(self):
        print('I am destructed', self.x)

tom = PartyAnimal("Tom")
tom.party()
tom.party()
tom = 42
print('an contains: ', tom)

ann = PartyAnimal("Ann")
ann.party()