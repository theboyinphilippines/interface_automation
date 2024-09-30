import logging

import yaml

from testcase.conftest import get_env


def read_yaml(filepath):
    with open(filepath,'r') as f:
        data = yaml.safe_load(f)
        return data

def get_host(get_env):
    data = read_yaml("./config/config.yaml")
    host = data["host"]
    return host


if __name__ == '__main__':
    get_host("test")
