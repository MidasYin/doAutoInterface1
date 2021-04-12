# #接口自动化模板
import requests
import pytest
from lib.get_yaml import doYaml
from settings import *
from lib.getLogging import Logger
logging = Logger("conftest").getlog()

# @pytest.fixture(scope="session", autouse=True)
# def loginPlatform():
#     rs = doYaml.get_data(os.path.join(BASE_PATH, "requestBJR.yaml"))
#     url = rs["url"] + rs["path"]
#     method = rs["method"]
#     data = rs["LoginPlatform"]
#     #login登录
#     try:
#         result = requests.session().request(method, url, json=data)
#         if result.status_code == 200:
#             rjson = result.json()
#             if rjson["MessageType"]==200:
#                 rsToken = rjson["Data"]["access_token"]
#             else:
#                 logging.info("登录失败，请稍后再试")
#         #print("用户二的token：%s" % rsToken)
#     except Exception as e:
#         logging.info("错误原因是:%s" % e)
#
#     yield rsToken
#     logging.info("开始清理临时数据...")


@pytest.fixture(scope="session", autouse=True)
def login():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "requestBJR.yaml"))
    url = rs["url"] + rs["path"]
    method = rs["method"]
    data = rs["Login"]
    #login登录
    try:
        result = requests.session().request(method, url, json=data)
        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"]==200:
                rsToken = rjson["Data"]["access_token"]
            else:
                logging.info("登录失败，请稍后再试")

    except Exception as e:
        logging.info("错误原因是:%s" % e)

    yield rsToken

    logging.info("开始清理临时数据...")


if __name__ == '__main__':
    pass
    #logging.info(login())







