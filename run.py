#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   run.py    
@Contact :   1276400081@qq.com
@License :   (C)Copyright 2021-2022, YYC-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/13 11:16   YYC      1.0         None
'''

from settings import *
import pytest
import os
from lib.fileGet import FileUtils
from caseCreate import batchCreateCase, templateFile



if __name__ == '__main__':
    batchCreateCase(case_fold=DATA_PATH, template_file=templateFile, path=CASE_PATH)
    FileUtils.rmtree(REPORT_PATH)
    pytest.main(["-s", "-v", "-q", CASE_PATH, "--reruns", "3", "--reruns-delay", "2", "--alluredir", "./report/allure-results"])  # 以alluredir运行生成报告，并保存在result文件中
    allure_cmd = "allure generate ./report/allure-results -o ./report/html --clean"  # 将报告转换成html格式文件的命令
    p = os.popen(allure_cmd, mode="r")  # 运行命令
    print(p.read())    # 打印查看结果