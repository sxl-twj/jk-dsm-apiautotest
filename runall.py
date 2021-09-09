import pytest
import allure
import datetime
import time
import os

if __name__ == '__main__':
    # now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # pytest.main(['--html=../report/report'+now_time+'.html'])

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('/Users/shenxiaoling/allure-2.14.0/bin/allure generate ./temp -o ./report --clean')