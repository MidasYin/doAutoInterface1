此框架使用方法：
1、在data目录下，按照请求格式，配置好http请求的数据
data下是按照yaml格式创建请求体，可以参照如何yaml文件的提取

如：
get方法：

method: get
path: 'xx'
data:

header:
  User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
  Content-Type: application/json

post方法：

method: post
path: 'xx'
data:
  AttachCount: 0
  SubList: [ ]
  SubList1:
    - 
      AdjustRate: false
      Amount: xx
      Id: ""
  SundryFees: 0
header:
  User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
  Content-Type: application/json


2、配置好后，使用run.py 执行
其中 data目录下可以嵌套多层目录，这边可以取出所有data下方，后缀是yaml的文件，并生成测试脚本 test_xx.py
不做修改的话，生成的 test_xx.py 会在testcase的目录下方
此函数就是批量生成用例的函数：在caseCreate.py函数中，有注释的，需要自定义到testcase的下级目录也行，
建议在这里，因为pytest是执行testcase下的所有test_xx.py用例

batchCreateCase(case_fold=DATA_PATH, template_file=templateFile, path=CASE_PATH)
 """

    :param case_fold: 取数据，以及生成的用例读取请求数据的目录
    :param template_file: 模板文件地址，templateFile
    :param path: 默认为CASE_PATH,即生成的用例在testcase目录下
    :return:
    """

3、用例执行过程中的日志在log文件里面

4、用例产生的报告在 report下，可以通过 在\report\html\index.html 跳转查看allure提供的用例


5、现在只做了请求，并返回result，没对进一步验证进行编写，这点可以修改template/templates.txt继续去完善
