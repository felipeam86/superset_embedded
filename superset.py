import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")
SECRET = os.getenv("SECRET")
URL_AUTH = os.getenv("URL_AUTH")
URL_GUEST_TOKEN = os.getenv("URL_GUEST_TOKEN")
USERNAME = os.getenv("USERNAME")
FIRST_NAME = os.getenv("FIRST_NAME")
LAST_NAME = os.getenv("LAST_NAME")


def authenticate(
    name=API_TOKEN,
    secret=SECRET,
):
    response = requests.post(
        URL_AUTH,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Access-Control-Allow-Origin": "http://localhost:8000",
        },
        data=json.dumps(
            {
                "name": name,
                "secret": secret,
            }
        ),
    )
    return response.json()["payload"]["access_token"]


def get_guest_token_for_dashboard(
    dashboard_id,
    access_token,
    username=USERNAME,
    first_name=FIRST_NAME,
    last_name=LAST_NAME,
):
    response = requests.post(
        URL_GUEST_TOKEN,
        data=json.dumps(
            {
                "user": {
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                "resources": [
                    {
                        "type": "dashboard",
                        "id": dashboard_id,
                    }
                ],
                "rls": [],
            }
        ),
        headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    return response.json()["payload"]["token"]
