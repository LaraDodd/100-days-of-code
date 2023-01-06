# making an args function
def add(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot


print(add(1, 6, 7, 8, 9))


# kwargs function
def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)  # prints a dictionary of kwargs


calculate(add=5, multiply=6)


def decrease_calc(number, **kwargs):
    new_num = number / kwargs["divide"]
    new_num = new_num - kwargs.get("minus")  # both kwargs["key"] and kwargs.get("key") can be used
    return new_num


print(decrease_calc(30, divide=6, minus=1))  # prints 4.0


# making a kwargs class
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.colour = kw.get("colour")


car = Car(make="mini")
print(car.make)  # prints mini
print(car.colour)  # prints None
