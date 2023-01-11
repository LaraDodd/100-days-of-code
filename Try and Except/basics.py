# try first piece of code, if doesn't work go into except code
try:
    file = open("my_file.txt")
except:
    file = open("my_file.txt", "w")

# except in code above has yeelow squiggly because program does not specifiy to the except
# what kind of error the except should excuse. E.g. code below works fine even though there is a
# key value error:
try:
    file = open("my_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["dfghjk"])
except:
    file = open("my_file.txt", "w")

# need to specify error type
try:
    file = open("my_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["dfghjk"])
except FileNotFoundError:
    file = open("my_file.txt", "w")
except KeyError:
    print("That key does not exist")

# can also specify the error message in the except, to make it clearer
try:
    file = open("my_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["dfghjk"])
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
except FileNotFoundError:
    file = open("my_file.txt", "w")

# if file did exist and key was correct, else would be called:
try:
    file = open("my_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["key"])
except FileNotFoundError:
    file = open("my_file.txt", "w")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
# this code is run no matter what
finally:
    file.close()
    print("The file is closed")

#=============================================================================
# e.g key error try and except where likes are zero for some posts
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:

    try:
        total_likes = total_likes + post["Likes"]

    except KeyError:
        pass

print(total_likes)

#============================================================
#e.g. index error
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
