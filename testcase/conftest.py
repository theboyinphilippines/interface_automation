import pytest
import requests
from database.mysql import Db

# 解析命令行参数
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        help="通过env添加自定义命令行参数指定测试环境名称"
    )

# 获取命令行参数值
@pytest.fixture()
def get_env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def get_token():
    base_url = "http://localhost:8081"
    # 发起请求
    data = {'username': "xixihaha", 'password': "123456"}
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(f"{base_url}/user/login", json=data, headers=headers).json()
    # 断言
    return resp["token"]

# 注册接口时，先删除已经注册的该用户
# @pytest.fixture(params=["username1","username2"])
# def delete_user(request):
#     user = request.param
#     db = Db(dbinfo= {
#     "host": "127.0.0.1",
#     "post" : 3306,
#     "user" : "root",
#     "password":"1234qwer!",
#     "database":"automation_db"
# })
#     db.dbcommit(sql='delete from automation_db where username = "%s";' % user)
#     db.dbclose()
#     return user



