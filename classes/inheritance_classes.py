#Super class
class LivingOrganism:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale.....Exhale")

class Fish(LivingOrganism):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()


