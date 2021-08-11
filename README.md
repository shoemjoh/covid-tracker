# covid-tracker
Freestyle project for NYU Stern: a daily covid tracker email update with relevant statistics

# To run with the required packages, create an environment and install the packages using pip install with the requirements.txt file. Code shown below:

conda create -n covid-env python=3.8 
conda activate covid-env
pip install -r requirements.txt 

# To run the program, use this command from the terminal:
python covid-tracker.py

# Set up some environment variables
# 1 - A sendgrid api key and sender email address:
SENDGRID_API_KEY = ""

# in production mode:
APP_ENV="production" COUNTRY_CODE="INDIA" python covid-tracker.py

# Make sure the settings are configured properly in sendgrid, single sender.