import requests
import os
import json


## product_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
#productx_url = "https://covid-19.dataflowkit.com/v1/world"
# write code here
# 1) View the data in the browser, 2) then make a request for the data, 3) then process the data.
# beautiful soup would process html looking responses
#
#
#response = requests.get(productx_url)
# print(type(response))  # <class 'requests.models.Response'>
# dir(response) - what can we do with the response object
#
# print(response.status_code)
# print(response.text)  # string data type
#
#y = json.loads(response.text)
# print(type(y))
#
#print(y["Active Cases_text"])


# Calculate and return percent change?
# Format

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_k")

url = "https://covid-19-tracking.p.rapidapi.com/v1"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
parsed_response = json.loads(response.text)
print(type(response.text))
print(type(parsed_response))
