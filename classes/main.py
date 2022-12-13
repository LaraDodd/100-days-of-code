class User:
    pass

user_1 = User()
user_2 = User()
print(user_1)

# add attribute to a specific object
user_1.name = "Lara"
user_2.name = "Jack"
print(user_1.name)
print(user_2.name)

# initialising attributes so that you don't have to create the same attribute for each object every time
class UserImproved:

    def __init__(self, name):
        print("new user created")
        self.name = name

#now everytime you create an object, you initialise the name attribute and have to assign it
user_3 = UserImproved("Sandy")
print(user_3.name)

#You can add more than one initialised attribute.
class UserImprovedEvenMore:

    def __init__(self, name, id):
        print("new user created")
        self.name = name
        self.id = id
        #you can also add attributes with default values so that you don't have to input them every time you create an object
        self.followers = 0

    user_4 =
