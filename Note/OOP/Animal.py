class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"name: {self.name}, is a {self.species}"

    def make_sound(self,sound):
        print(f"{self.name} can {sound}")

