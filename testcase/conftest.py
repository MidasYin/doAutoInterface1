# #接口自动化模板
import requests
import pytest
import lib
import time
from _pytest import runner, terminal
from lib.get_yaml import doYaml
from lib.requestDingDing import RequestDing
from lib.requestQiWeiXin import RequestQi
from settings import *
from lib.getLogging import Logger
logging = Logger("conftest").getlog()

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
        logging.info("错误原因是:{}" % e)

    yield rsToken

    logging.info("开始清理临时数据...")

def pytest_terminal_summary(terminalreporter, sendType = SENDTYPE, switch = SWITCH):
    """
    :param terminalreporter:
    :param sendType: DingDing,QiWeiXin,Email
    :param switch: True or False
    :return:
    """
    duration = time.time() - terminalreporter._sessionstarttime
    msg = {
        "total": terminalreporter._numcollected,
        "passed": len(terminalreporter.stats.get('passed', [])),
        "failed": len(terminalreporter.stats.get('failed', [])),
        "error": len(terminalreporter.stats.get('error', [])),
        "skipped": len(terminalreporter.stats.get('skipped', [])),
        "duration": "{:.2f}".format(duration)
    }
    logging.info("开始统计用例执行情况...")
    logging.info(50 * "---")
    logging.info(msg)
    logging.info(50 * "---")
    if switch:
        if sendType == "DingDing":
            logging.info("开始发送钉钉报告...")
            RequestDing.sendDingMsg(webhook=DINGDINGURL, msg=RequestDing.getMsg(msg))
        elif sendType == "QiWeiXin":
            logging.info("开始发送企业微信报告...")
            RequestQi.sendQiMsg(webhook=QIWEIXINURL, msg=RequestQi.getMsg(msg))
        elif sendType == "Email":
            logging.info("待开发")
        else:
            raise Exception("不支持其他发送方式")
    else:
        logging.info("不发送报告")



if __name__ == '__main__':
    pass
    #logging.info(login())







