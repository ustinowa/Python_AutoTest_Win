import json

import requests
import yaml

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)


def registry():
    headers = {
        'Content-Type':'application/json'
    }
    data = {
        "name":d['username'],
        "email":"Developer_283@gmail.com",
        "password":d['password']
    }
    res = requests.post(url=d['url_reg'], data=json.dumps(data), headers=headers)
    return res.json()["data"]["Token"]


def auth():
    headers = {
        'Authtorization': f'Bearer {d["token"]}'
    }
    data = {
        'e-mail':'Developer_283@gmail.com',
        'password':d['password']
    }
    res = requests.post(url=d["url_auth"], headers=headers, data=json.dumps(data))
    print(res.content)

