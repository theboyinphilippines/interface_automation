import allure
import pytest
from common.handle_request import send_request_token
from common.handle_yaml import read_yaml


@allure.epic("tmall在线购物平台接口测试")
@allure.feature("用户模块")
class TestUser:
    @allure.story("用户信息测试")
    @allure.title("异常用例--用户信息")
    @allure.description("用户信息,用户id不存在")
    @pytest.mark.parametrize("test_data", read_yaml("./data/user/user.yaml"))
    def test_user01(self, test_data,get_token,get_env):
        send_request_token(test_data, get_token,get_env)


if __name__ == '__main__':
    pytest.main()
