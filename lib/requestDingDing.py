#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   requestDingDing.py    
@Contact :   1276400081@qq.com
@License :   (C)Copyright 2021-2022, YYC-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/15 11:43   YYC      1.0         None
'''
import requests
import logging
from settings import *


class RequestDing():

    @staticmethod
    def sendDingMsg(webhook, msg):
        header = {
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 50.0.2661.102Safari / 537.36",
            "Content-Type": "application/json; charset=UTF-8"
            }
        msg_body = {
            "msgtype": "markdown",
            "markdown": msg,
            "at": {
                #"atMobiles": [***],
                "isAtAll": True
            }
        }

        try:
            res = requests.request(url= webhook, method="post", json=msg_body, headers=header)
            result = res.json()

        except Exception as e:
            logging.error("请求异常，原因是：{}".format(e))
            result = None

        return result

    @staticmethod
    def getMsg(resultDict:dict) -> dict:
        """

        :param resultDict: 测试结果返回的数据
        :return: 数据处理后的msg 字典

        """
        if isinstance(resultDict, dict):
            Msg = {
                "title": "zidonghua",
                "text": "### 自动化接口测试结果\n\n"
                        "> **total**: {}".format(resultDict["total"]) + "\n\n"
                        "> **passed**: {}".format(resultDict["passed"]) + "\n\n"
                        "> **failed**: {}".format(resultDict["failed"]) + "\n\n"
                        "> **error**: {}".format(resultDict["error"]) + "\n\n"
                        "> **skipped**: {}".format(resultDict["skipped"]) + "\n\n"
                        "> **duration**: {}".format(resultDict["duration"]) + "second \n\n"
                }
            return Msg

        else:
            raise TypeError("传递类型错误")





if __name__ == '__main__':

    webhook = DINGDINGURL
    msg = {
        "total": 12,
        "passed": 12,
        "failed": 0,
        "error": 0,
        "skipped": 0,
        "duration": 3.01
        }

    Msg = RequestDing.getMsg(msg)

    print(Msg)
    print(RequestDing.sendDingMsg(webhook, Msg))
