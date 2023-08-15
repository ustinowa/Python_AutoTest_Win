import json
import pytest
import requests
import yaml

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)


def auth():
    data = {
        "username": d["username"],
        "password": d["password"]
    }
    res = requests.post(url=d["url_auth"], data=json.dumps(data))
    return res.json()["token"]


@pytest.fixture()
def create_post():
    token = auth()
    headers = {
        "X-Auth-Token": token
    }
    data = {
        "title": "my_title",
        "description": "my_description",
        "content": "my_content",
    }
    res = requests.post(url=d["url_create"], headers=headers, data=data)
    return res.json()["description"]

