class PartyAnimal:
    x = 0 

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

z = PartyAnimal()

h = PartyAnimal()

an.party()
an.party()
an.party()

z.party()

print(PartyAnimal.party(h))
