import requests
import os
import json


from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_k")
home_c = os.getenv("home_country")


url = "https://covid-19-tracking.p.rapidapi.com/v1"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
parsed_response = json.loads(response.text)


# print(response.text)
print(parsed_response)


# def set_country():
#    if APP_ENV == "development":
#        user_country = input("PLEASE INPUT A COUNTRY CODE (e.g. 'US'): ")
#    else:
#        user_country = home_c
#    return user_country


for x in parsed_response:
    if x["Country_text"] == home_c:
        print(
            f"The total case count in {home_c} is: ", x["Total Cases_text"])
        break


# def set_geography():
#    if APP_ENV == "development":
#        user_country = input("PLEASE INPUT A COUNTRY CODE (e.g. 'US'): ")
#        user_zip = input("PLEASE INPUT A ZIP CODE (e.g. 20057): ")
#    else:
#        user_country = COUNTRY_CODE
#        user_zip = ZIP_CODE
#    return user_country, user_zip
#
