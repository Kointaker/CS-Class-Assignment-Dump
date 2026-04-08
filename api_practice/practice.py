import requests



# use requests.get() to get the data response from the API
url = "https://api.portfoliooptimizer.io/v1/portfolio/optimization/minimum-variance"
# print the response using the json() method
response = requests.post(
    "https://api.portfoliooptimizer.io/v1/portfolio",
    json={'assets': 2, 'assetsCovarianceMatrix': [[0.0025, 0.0005], [0.0005, 0.0100]]}
    
)


print("Portfolio Data:")
print(response)
print("")

### extra
# print out the status code of the response
print("Status Code:")
print(response.status_code)
# print specific parts of the data (hint doesn't the data look familiar? Maybe like a dictionary, and lists?)
