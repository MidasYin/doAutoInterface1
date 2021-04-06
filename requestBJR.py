import requests
from lib.get_yaml import doYaml
from settings import *


def loginPlatform():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "requestBJR.yaml"))
    url = rs["url"] + rs["path"]
    method = rs["method"]
    data = rs["LoginPlatform"]
    #login登录
    try:
        result = requests.session().request(method, url, json=data)
        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"]==200:
                rsToken = rjson["Data"]["access_token"]
            else:
                print("登录失败，请稍后再试")
        #print("用户二的token：%s" % rsToken)
        return rsToken

    except Exception as e:
        print("错误原因是：%s" % e)

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
                print("登录失败，请稍后再试")
        #print("用户一的token：%s" % rsToken)
        return rsToken

    except Exception as e:
        print("错误原因是：%s" % e)

if __name__ == '__main__':

    pass