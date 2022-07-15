from OOP.Animal import Animal

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.bread = breed
        self.toy = toy

    def play_toy(self):
        print(f"{self.name} is playing {self.toy}")

        