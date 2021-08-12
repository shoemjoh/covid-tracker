# covid-tracker
Freestyle project for NYU Stern: a daily covid tracker email update with relevant statistics

# First, create a project specific environment.
```
conda create -n covid-env python=3.8 
conda activate covid-env
```
# Install the packages required for the application.
```
pip install -r requirements.txt 
```
# To run the program, use this command from the terminal:
```
python covid_tracker.py
```
# Environment variables stored on the Heroku server. Run with the following command:
```
heroku run bash
```
# To run in production mode and specific a particular country:
```
APP_ENV="production" COUNTRY_CODE="INDIA" python covid-tracker.py
```

# Visualize this covid information on a web application by running:
```
FLASK_APP=web_app flask run
```
# And then searching for the following url:
```
http://localhost:5000/country/cases.json
```