import requests
import datetime
import pytest
import json


class TestSendResquest:

    access_token = ""
    session = requests.session()

    def setup(self):
        print("在每个测试用例之前进行运行")

    def teardown(self):
        print("在每个测试用例之后进行运行")
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_get_token(self):
        url = "http://192.168.3.18/itsm/itsmboot/user/login"
        data = {
            "login": "admin",
            "loginType": "system",
            "password": "Password@1",
            "roleLoginType": 0
        }

        rep = TestSendResquest.session.request(method='post', url=url, json=data)
        print(rep.json())
        TestSendResquest.access_token = rep.json()["sessionId"]

    @pytest.mark.skip(reason='不用执行该接口')
    def test_get_current(self):
        url = "http://192.168.3.18/itsm/itsmboot/person/current"
        data = {
            "loginType": 0
        }
        # headers = {
        #     "Authorization": TestSendResquest.access_token,
        #     "Content-Type": "application/json;charset=UTF-8"
        # }
        rep = TestSendResquest.session.request(method='get', url=url, params=data)
        print(rep.json())


# if __name__ == '__main__':
#     now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     print(now_time)
#     pytest.main(['--html=../report/report'+now_time+'.html'])
