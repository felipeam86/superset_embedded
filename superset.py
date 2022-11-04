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
FIRST_NAMER = os.getenv("FIRST_NAMER")
LAST_NAME = os.getenv("LAST_NAME")


def authenticate():
    response = requests.post(
        URL_AUTH,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Access-Control-Allow-Origin": "http://localhost:8000"
        },

        data=json.dumps(
            {
                "name": API_TOKEN,
                "secret": SECRET,
            }
        ),
    )
    return response.json()["payload"]["access_token"]


def get_guest_token_for_dashboard(dashboard_id, access_token):
    response = requests.post(
        URL_GUEST_TOKEN,
        data=json.dumps(
            {
                "user": {
                    "username": USERNAME,
                    "first_name": FIRST_NAMER,
                    "last_name": LAST_NAME,
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
