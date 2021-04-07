import requests
class Request:
    def __init__(self):
        self.num_calls = 0
        # self.method = method
        # self.url = url
        self.session = requests.session()

    def __call__(self, func):
        self.num_calls += 1
        self.func = func

        def fun_wrapper(*args, **kwargs):
            rst = self.requestMethod(*args, **kwargs)
            self.func(*args, **kwargs)
            return rst
        return fun_wrapper

    def requestMethod(self, *args, **kwargs):
        try:
            if 'data' in kwargs.keys():
                result = self.session.request(method=kwargs['method'], url=kwargs['url'], headers=kwargs['headers'], json=kwargs['data'])
            else:
                result = self.session.request(method=kwargs['method'], url=kwargs['url'], headers=kwargs['headers'])
            if result.status_code == 200:
                result.encoding = 'utf-8'
                rjson = result.text
                return rjson
            else:
                return result.json()
        except Exception as e:
            print("request 错误原因是：%s" % e)

    def closeSession(self):
        return self.session.close()

if __name__ == '__main__':


    @Request()
    def getJd(*args, **kwargs):
        print("ddd")
    print(getJd(method='get', url='http://www.baidu.com'))

