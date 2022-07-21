class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print("I heard there were monster running around last night")


# Define your classes below:

class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    # def __init__(self):
    #     super().__init__(self)
    pass


class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        print(f"{self.num_cars} car train")

    def __len__(self):
        return self.num_cars

