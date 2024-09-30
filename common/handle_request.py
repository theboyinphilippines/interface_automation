import json
import logging

import requests

from common.handle_yaml import get_host
from testcase.conftest import get_env


def send_request(test_data,get_env):
    base_url = get_host(get_env)
    data = test_data["data"]["data"][get_env]
    headers = test_data["data"]["headers"]
    if test_data["data"]["requestType"] == "params":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], params=data,
                                headers=headers).json()
    elif test_data["data"]["requestType"] == "json":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], json=data,
                                headers=headers).json()
    elif test_data["data"]["requestType"] == "data":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], data=data,
                                headers=headers).json()
    else:
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], files=data,
                                headers=headers).json()

    # 断言
    print(resp)
    assert resp["code"] == test_data["data"]["assert"]["code"]
    assert resp["msg"] == test_data["data"]["assert"]["msg"]


def send_request_token(test_data,token,get_env):
    base_url = get_host(get_env)
    data = test_data["data"]["data"][get_env]
    headers = test_data["data"]["headers"]
    headers["x-token"] = token
    if test_data["data"]["requestType"] == "params":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], params=data,
                                headers=headers).json()
    elif test_data["data"]["requestType"] == "json":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], json=data,
                                headers=headers).json()
    elif test_data["data"]["requestType"] == "data":
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], data=data,
                                headers=headers).json()
    else:
        resp = requests.request(test_data["data"]["method"], f"{base_url}" + test_data["data"]["url"], files=data,
                                headers=headers).json()

    # 断言
    assert resp["code"] == test_data["data"]["assert"]["code"]
    assert resp["msg"] == test_data["data"]["assert"]["msg"]
