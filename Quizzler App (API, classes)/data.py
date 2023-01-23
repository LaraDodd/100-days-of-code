import requests
"""this module gets data from quizzler api"""

response = requests.get(url="https://opentdb.com/api.php?amount=15&type=boolean")
print(response.raise_for_status())

data = response.json()

question_data = data["results"]
