import requests
import os
import json


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


# print(response.text)
# print(parsed_response)

home_country = input("Please enter your home country: ")

for x in parsed_response:
    if x["Country_text"] == home_country:
        print(
            f"The total case count {home_country} is: ", x["Total Cases_text"])
        break
