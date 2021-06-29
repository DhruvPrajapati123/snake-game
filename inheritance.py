class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swimming")

    def breathe(self):
        super().breathe()
        print("Underwater")


fish = Fish()
fish.swim()
fish.breathe()
print(fish.num_of_eyes)
