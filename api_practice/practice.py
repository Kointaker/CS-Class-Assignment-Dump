import requests



# use requests.get() to get the data response from the API
url = "https://bored-api.appbrewery.com/random"




response = requests.get(url)

# 4. Print the status code
print(response.status_code)

# 5. Print the JSON response
print(response.json())






