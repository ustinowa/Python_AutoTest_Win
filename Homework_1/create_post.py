import json
import requests
import yaml

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)


def auth():
    headers = {
        'X-Auth-Token': d['token']
    }
    data = {
        'username': d['username'],
        'password': d['password']
    }
    res = requests.post(url=d["url_auth"], headers=headers, data=json.dumps(data))
    print(res.content)


def create_post():
    data = {
        "title": "my_title",
        "description": "my_description",
        "content": "my_content"
    }
    res = requests.post(url=d["url_create"], data=json.dumps(data))
    print(res.content)

create_post()