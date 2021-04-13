import sys
import os
from settings import *
from lib.create_cases import case_create
from lib.fileGet import FileUtils

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
    """

    :param file:
    :param template_file:
    :param path: 执行用例的目录
    :return:
    """
    case_create(file=file, template_file=template_file)
    caseName = file.split(".")[0]
    print("执行用例:{}_{}".format("test", caseName))
    file = os.path.join(path, "test_" + caseName + ".py")
    os.system("pytest" + " " + "-sv" + " " + file)

def batchRunCase(dataPath:str, template_file = templateFile, path=CASE_PATH):
    """

    :param dataPath: 批量生成case的目录
    :param template_file:
    :param path:
    :return:
    """
    if FileUtils.isexists(dataPath):
        try:
            file_lists = os.listdir(dataPath)  # 取出data目录下的所有文件
            for file in file_lists:
                runCase(file=file, template_file=template_file, path=path)
        except Exception as e:
            print("批量生成case失败，原因是:{}".format(e))
    else:
        raise Exception("当前路径不存在")


if __name__ == '__main__':
    # runCase(file="rentin.yaml", template_file=templateFile)
    # runCase(file="bill.yaml", template_file=templateFile)
    batchRunCase(DATA_PATH, templateFile)


