import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response) # doesn't print out data, but instead a response code

# creating a new dictionary
my_dict = {"Java": 100, "Python": 112, "C": 11}

# one-liner

print("One line Code Key value: ", list(my_dict.values()))
