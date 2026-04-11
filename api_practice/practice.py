import requests



# use requests.get() to get the data response from the API
url = "https://bored-api.appbrewery.com/random"


# From documentation:
# using this link (https://bored-api.appbrewery.com/filter?type=education) will return educational type activities
# using this link (https://bored-api.appbrewery.com/activity/3943506) will return a specific activity

response = requests.get(url)

# 4. Print the status code
print(response.status_code)

# 5. Print the JSON response
print(response.json())






