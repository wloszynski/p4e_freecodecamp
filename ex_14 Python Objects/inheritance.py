class PartyAnimal:
    x = 0
    name = ''
    # constructor with variab;e
    def __init__(self, nam):
        self.name = nam
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far', self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


j = PartyAnimal("James")
j.party

t = FootballFan("Tim")
t.party()
t.touchdown()