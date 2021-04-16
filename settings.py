import os

#设置目录的绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, 'data')   #yaml测试用例存放位置
CASE_PATH = os.path.join(BASE_PATH, "testcase") #测试用例存放位置
REPORT_PATH = os.path.join(BASE_PATH, 'report')  #测试报告存放位置
TEMP_PATH = os.path.join(BASE_PATH, 'testcase/temp')  #存放临时用例位置
LOG_PATH = os.path.join(BASE_PATH, 'log')  #存放日志目录
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template') #存放用例生成模板文件


#设置系统接口的域名地址
URL = "xx"

#设置pymysql相关配置
ip = 'xx'
port = 'yy'  #测试数据库端口
#port = '5442'  #dev数据库端口
user = 'ss'
password = '123456'
database = 'dd'

#配置redis

#是否发送报告
SWITCH = True
#SWITCH = False

#设置请求钉钉的地址
DINGDINGURL = ""


#设置企业微信请求地址
QIWEIXINURL = "xx"


#设置结果发送平台(DingDing,QiWeiXin,Email)
SENDTYPE = "DingDing"
#SENDTYPE = "QiWeiXin"
#SENDTYPE = "Email"



