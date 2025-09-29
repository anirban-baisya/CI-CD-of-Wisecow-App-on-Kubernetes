"""
Application Health Checker
-------------------------
Checks if a web application is 'up' or 'down' by requesting its URL and inspecting the HTTP status code.

How to run:
$ python check_app_health.py

Dependencies:
- requests (install with: pip install -r requirements.txt)

Add 'APP_URL' variable for with the URL of my application.
"""

import requests

APP_URL = "http://a475995a7407440f3915fd8609d72f3b-549440630.us-east-1.elb.amazonaws.com/"  # change this to our application's URL

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        print(f"HTTP Status Code: {status_code}")
        if status_code == 200:
            print("Application is UP and functioning correctly.")
        else:
            print(f"Application is DOWN or not responding correctly. Status code: {status_code}")
    except requests.exceptions.RequestException as e:
        print("Application is DOWN or not reachable.")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("---- Application Health Checker ----")
    check_app_health(APP_URL)
    print("------------------------------------")