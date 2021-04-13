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

#可执行文件list
path_read = []


def runCase(file:str, case_fold=DATA_PATH, template_file = templateFile, path=CASE_PATH) ->bool:
    """

    :param file:
    :param template_file:
    :param path: 执行用例的目录
    :return:
    """
    case_create(file=file, template_file=template_file, case_fold=case_fold)
    caseName = file.split(".")[0]
    print("执行用例:{}_{}".format("test", caseName))
    file = os.path.join(path, "test_" + caseName + ".py")
    os.system("pytest" + " " + "-sv" + " " + file)


def batchRunCase(case_fold=DATA_PATH, template_file = templateFile, path=CASE_PATH):
    """

    :param case_fold: 取数据，以及生成的用例读取请求数据的目录
    :param template_file: 模板文件地址，templateFile
    :param path: 默认为CASE_PATH,即生成的用例在testcase目录下
    :return:
    """

    file_lists = check_if_dir(case_fold)
    for file in file_lists:
        #分离文件以及目录，分别用于创建用例
        file_name = file.split("\\")[-1]
        case_fold = os.path.dirname(file)
        try:
            runCase(file=file_name, template_file=template_file, case_fold=case_fold, path=CASE_PATH)
        except Exception as e:
            print("批量生成case失败，原因是:{}".format(e))


def check_if_dir(file_path: str) -> list:
    """

    :param file_path: 需要查询文件的根目录
    :return: 返回所有yaml或者yml文件的目录
    """
    temp_list = os.listdir(file_path)    #put file name from file_path in temp_list
    for temp_list_each in temp_list:
        if os.path.isfile(os.path.join(file_path, temp_list_each)):
            temp_path = os.path.join(file_path, temp_list_each)
            if os.path.splitext(temp_path)[-1] == '.yaml' or os.path.splitext(temp_path)[-1] == '.yml':    #自己需要处理的是.yaml或者yml文件所以在此加一个判断
                path_read.append(temp_path)
            else:
                continue
        else:
            check_if_dir(os.path.join(file_path, temp_list_each))
    return path_read


if __name__ == '__main__':
    # runCase(file="rentin.yaml", template_file=templateFile)
    # runCase(file="bill.yaml", template_file=templateFile)
    #pathOne = os.path.join(DATA_PATH, "base")
    batchRunCase(case_fold=DATA_PATH, template_file=templateFile, path=CASE_PATH)


