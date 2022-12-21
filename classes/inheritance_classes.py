# Super class
class LivingOrganism:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale.....Exhale")

    def move(self):
        print("I can walk!")


#  normal class which calls upon the super class
class Fish(LivingOrganism):
    def __init__(self):
        super().__init__()  # must call the super class and initialise it on this class's init

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()


class Bird(LivingOrganism):
    def __init__(self):
        super().__init__()
        self.num_eyes = 3

    def squark(self):
        print("CA CAHHH!!!")

    # can also add to existing methods in the super class
    def movement(self):
        self.move()
        print("I can fly!")


robbie_robin = Bird()
robbie_robin.movement()
