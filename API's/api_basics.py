import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)  # doesn't print out data, but instead a response code

response.raise_for_status() #get specific response error message if there is one

data = response.json() # convert api response object into json data
print(data)
print(data["timestamp"]) # pull specific info out of json data


