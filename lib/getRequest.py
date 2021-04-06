#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   getRequest.py    
@Contact :   1276400081@qq.com
@License :   (C)Copyright 2021-2022, YYC-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/26 11:17   YYC      1.0         None
'''
import inspect

class Request:

    def __init__(self, url='', method='get'):
        ''''''
        self.url = url  # 请求路径
        self.method = method # 请求方法
        self.func_return = None # 被装饰器标记的方法的返回参数
        self.func_im_self = None  # 被装饰器标记的方法的类的实例
        self.session = None # 当前使用的会话对象

    def __call__(self, func):
        self.func = func
        self.is_class = False
        try:
            if inspect.getfullargspec(self.func).args[0] == 'self':
                self.is_class = True
        except IndexError:
            pass

        def fun_wrapper(*args, **kwargs):
           # 调用被装饰标记的方法，这个方法会返回请求接口所需要的返回值
            self.func_return = self.func(*args, **kwargs) or {}
            self.func_im_self = args[0] if self.is_class else object
            self.create_url()
            self.create_session()
            self.session.headers.update(getattr(self.func_im_self, 'headers', {}))
            self.decorator_args.update(getattr(self.func_im_self, 'common_params', {}))
            self.decorator_args.update(self.func_return)

            return Request(self.method, self.url, self.session)
        return fun_wrapper

class AdvertService:

    def __init__(self):
        self.common_params = {} # 定义接口请求的公共参数
        self.headers = {} # 定义请求的header
        self.base_url = self._config.AD_ADMIN_ROOT_URL

    # @Request(url=“/v3/advert/create”, method='post')
    # def _create_ad(self, advert: Advert):
    #     return dict(json=advert)
