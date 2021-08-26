import pandas as pd
import argparse
import csv
import os
import traceback
import json
from sklearn.metrics import f1_score


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--testDataPath", help='真实数据的路径', type=str, default='A_rand.csv')
    parser.add_argument("--submitDataPath", help='提交数据的路径', type=str,
                        default='answer3.csv')
    parser.add_argument("--sep", help='分隔符', type=str, default=',')
    parser.add_argument("--labelName", help='label列名', type=str, default='label')

    return parser.parse_args()


# 比赛算分的核心逻辑,除此之外其他地方不要修改
def cal_score(testDataPath, submitDataPath, args):
    testData = pd.read_csv(testDataPath, sep=args.sep)
    submitData = pd.read_csv(submitDataPath, sep=args.sep)
    temp12 = pd.merge(testData, submitData, how="left", on="No.")
    logo_f1 = f1_score(temp12["logo_x"], temp12["logo_y"], average='micro')
    num_f1 = f1_score(temp12["tel_x"], temp12["tel_y"], average='micro')
    sign_f1 = f1_score(temp12["sign_x"], temp12["sign_y"], average='micro')
    multiple_f1 = (0.5 * logo_f1) + (0.25 * num_f1) + (0.25 * sign_f1)
    return multiple_f1


def calculate_score(args):
    testDataPath = args.testDataPath
    submitDataPath = args.submitDataPath

    resultCode = "0"
    resultMsg = "成功";
    if not os.path.exists(testDataPath):
        resultCode = "-1"
        resultMsg = "标准答案文件不存在"
    elif not os.path.exists(submitDataPath):
        resultCode = "-1"
        resultMsg = "结果文件不存在"
    elif ".csv" not in testDataPath:
        resultCode = "-1"
        resultMsg = "标准答案文件格式错误"
    elif ".csv" not in submitDataPath:
        resultCode = "-1"
        resultMsg = "结果文件格式错误"
    elif os.stat(testDataPath).st_size == 0:
        resultCode = "-1"
        resultMsg = "标准答案文件内容为空"
    elif os.stat(submitDataPath).st_size == 0:
        resultCode = "-1"
        resultMsg = "结果文件内容为空"
    else:
        labels_dict = {}
        output_dict = {}
        res = 0
        try:
            labels = csv.reader(open(testDataPath, 'r'))
        except Exception as e:
            resultCode = "-1"
            resultMsg = "标准答案文件格式错误"

        try:
            output = csv.reader(open(submitDataPath, 'r'))
        except Exception as e:
            resultCode = "-1"
            resultMsg = "结果文件格式错误"

        try:
            for one_item in enumerate(output):
                pred_cls = one_item[1][1]
                output_dict[one_item[1][0]] = pred_cls
        except Exception as e:
            resultCode = "-1"
            resultMsg = "结果文件内容格式错误"

        try:
            for one_item in enumerate(labels):
                lab_cls = one_item[1][1]
                labels_dict[one_item[1][0]] = lab_cls
        except Exception as e:
            resultCode = "-1"
            resultMsg = "标准答案文件内容格式错误"


        try:

            res = cal_score(testDataPath, submitDataPath, args)  # 算分核心函数
        except Exception as e:
            resultCode = "-1"
            resultMsg = "标准答案和结果内容格式不一致，请检查文件标题，答案行数，以及No.列是否正确"
            traceback.print_exc()

    scores = {}
    scores["score"] = res
    scores["resultCode"] = resultCode
    scores["resultMsg"] = resultMsg
    print(json.dumps(scores))


def run():
    args = parse_args()
    calculate_score(args)


if __name__ == '__main__':
    run()