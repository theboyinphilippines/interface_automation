import allure
import pytest
from common.handle_request import send_request
from common.handle_yaml import read_yaml


@allure.epic("tmall在线购物平台接口测试")
@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录接口测试")
    @allure.title("异常用例--登录")
    @allure.description("登录,用户名不存在")
    @pytest.mark.parametrize("test_data", read_yaml("./data/login/login.yaml"))
    def test_login01(self, test_data, get_env):
        send_request(test_data, get_env)


if __name__ == '__main__':
    pytest.main()
