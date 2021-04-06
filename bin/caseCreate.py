import sys
import os
from settings import *
from lib.create_cases import case_create

#将当前项目的目录加入零时环境变量，避免在其他地方运行时会出现引入错误
base_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(base_path)

#testcase创建目录
path = CASE_PATH

#template文件地址
templateFile = os.path.join(TEMPLATE_PATH, "templates.txt")

#查询yml文件的目录
foldname = "Position"

#yml文件的二级目录为

def runCase(file:str, template_file = templateFile, path=CASE_PATH) ->bool:
    case_create(file=file, template_file=template_file)
    caseName = file.split(".")[0]
    print("执行用例:{}_{}".format("test", caseName))
    file = os.path.join(path, "test_" + caseName + ".py")
    os.system("python" + " " + file)

if __name__ == '__main__':
    # 首先调用生成用例函数
    # create_case_file(_path=path, files="deleteEducations.yaml") #指定路径，创建指定文件的测试代码
    #case_create(file="rentin.yaml", template_file=templateFile)
    runCase(file="rentin.yaml", template_file=templateFile)


