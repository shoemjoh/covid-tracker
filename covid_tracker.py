import requests
import os
import json

from email_service import send_email
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("api_k")
HOME_C = os.getenv("home_country")
APP_ENV = os.getenv("APP_ENV", default="development")


def set_country():
    if APP_ENV == "development":
        user_country = input("PLEASE INPUT A COUNTRY CODE (e.g. 'USA'): ")
    else:
        print("Other mode")
        user_country = HOME_C
    return user_country

# Finding the total number of cases, updated daily, for the specified country.


country_chosen = set_country()


def get_cases(country_id):
    url = "https://covid-19-tracking.p.rapidapi.com/v1"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    parsed_response = json.loads(response.text)

    for x in parsed_response:
        if x["Country_text"] == country_id:
            country_cases = x["Total Cases_text"]
            return country_cases
    return print("No country match found.")


if __name__ == "__main__":
    print(
        f"RUNNING THE COVID TRACKER SERVICE IN {APP_ENV.upper()} MODE...")

    # Get data from get_cases function.
    print("Country:", country_chosen)

    result = get_cases(country_id=country_chosen)
    if not result:
        print("INVALID GEOGRAPHY. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    print(f"The total COVID-19 case count for {country_chosen} is: ", result)

    # Send and email with the results.
    html = ""
    html += f"As of this morning, the total COVID-19 case count for {country_chosen} is: {result}"

    send_email(subject="Daily Covid Briefing", html=html)
