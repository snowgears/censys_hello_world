import requests
import os
from dotenv import load_dotenv
from datetime import date

# first load the environment variables
load_dotenv()

CENSYS_API_KEY = os.getenv("CENSYS_API_KEY")
CENSYS_ENDPOINT = "https://app.censys.io/api"

# --- functions ---

# this formats a date in ISO 8601 format, for example YYYY-MM-DD
def format_date(date):
    d = date.strftime('%Y-%m-%d')
    return d

# Retrieve host counts by cloud. Hosts found after start_date will be included in the new asset counts.
def get_clouds_host_counts(start_date):
    url = CENSYS_ENDPOINT + f"/v1/clouds/hostCounts/{format_date(start_date)}"

    payload={}
    headers = {
        "Content-Type": "application/json",
        "censys-api-key": f"{CENSYS_API_KEY}"
    }
    
    response = requests.get(url, headers=headers, params=payload)

    data = response.text
    return data

# --- main thread ---

count = get_clouds_host_counts(date(2021, 1, 1))
print(count)