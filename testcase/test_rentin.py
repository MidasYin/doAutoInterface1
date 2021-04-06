#接口自动化模板
import json
from requestBJR import login, loginPlatform
from lib.get_yaml import doYaml
from settings import *
from lib.doRequest import Request
from lib.getLogging import Logger

#生成filename.log文件
filename = os.path.basename(__file__)
logging = Logger(filename).getlog()
featureName = filename.split(".")[0].split("_")[1] + "接口测试"

class TestRentin():
    def getRequestData(self,file: str) -> dict:
        """

        :param file: 读取yaml文件名
        :return: dict 返回数据解析

        """
        rs = doYaml.get_data(os.path.join(DATA_PATH, file))
        url = URL + rs["path"]
        method = rs["method"]
        data = rs["data"]
        header = rs["header"]
        return dict(url=url, method=method, data=data, header=header)


    @Request()
    def doRequest(self, **kwargs):
        logging.info("请求参数为:{}".format(kwargs))
        logging.info(50 * "---")

    def getResult(self, auth: str, **kwargs) -> bool:
        """

        :param auth:
        :return: bool
        """
        # 获取auth,组成新的header
        Authorization = auth
        headers = {**kwargs['header'], **{"Authorization": Authorization}}
        if kwargs['data']!= None:
            rs = self.doRequest(method=kwargs['method'], url=kwargs['url'], headers=headers, data=kwargs['data'])
        else:
            rs = self.doRequest(method=kwargs['method'], url=kwargs['url'], headers=headers)
        return rs


if __name__ == '__main__':
    Rentin = TestRentin()
    dataList = Rentin.getRequestData('rentin.yaml')
    logging.info("返回结果为:{}".format(Rentin.getResult(login(), method=dataList['method'], url=dataList['url'], header=dataList['header'], data=dataList['data'])))
    logging.info(50 * "---")
    #logging.info("返回结果为:{}".format(Rentin.getResult(loginPlatform(), method=dataList['method'], url=dataList['url'], header=dataList['header'], data=dataList['data'])))
    #logging.info(50 * "---")

