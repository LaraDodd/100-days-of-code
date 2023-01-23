import requests
"""this module gets data from quizzler api"""

param_dict = {"type": "boolean",
              "amount": "15",}

response = requests.get(url="https://opentdb.com/api.php", params=param_dict)
print(response.raise_for_status())

data = response.json()

question_data = data["results"]

print(question_data)