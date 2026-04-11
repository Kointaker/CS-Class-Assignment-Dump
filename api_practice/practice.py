import requests



# use requests.get() to get the data response from the API
url = "https://api.weather.gov/"



# 3. Make the request
# If your API uses GET with query parameters:
# response = requests.get(url, params=payload)
# If it uses POST with JSON body (more common for optimizers):
response = requests.get(url)

# 4. Print the status code
print(response.status_code)

# 5. Print the JSON response
print(response)






