# -*- coding: gbk -*-
import csv
import pandas as pd

signup_path = r"D:\doc\2358951845\FileRecv\2021年四川电信AI劳动竞赛报名信息.xlsx"
signup = pd.read_excel(signup_path)
signup = pd.read_excel(signup_path)

team_num = len(signup)
team_list = []
# team_list: [[..], [..], [..]]
for i in range(team_num):
    tmp_list = []
    if isinstance(signup["队员4姓名"][i], str):
        tmp_list = [i + 1, signup["团队名称"][i], 5, signup["队长姓名"][i], signup["队长电话"][i],
                    signup["队员1姓名"][i], signup["队员2姓名"][i], signup["队员3姓名"][i], signup["队员4姓名"][i]]
    else:
        if isinstance(signup["队员3姓名"][i], str):
            tmp_list = [i + 1, signup["团队名称"][i], 4, signup["队长姓名"][i], signup["队长电话"][i],
                        signup["队员1姓名"][i], signup["队员2姓名"][i], signup["队员3姓名"][i]]
        else:
            tmp_list = [i + 1, signup["团队名称"][i], 3, signup["队长姓名"][i], signup["队长电话"][i],
                        signup["队员1姓名"][i], signup["队员2姓名"][i]]
    team_list.append(tmp_list)

mark_detail_path = r"D:\doc\2358951845\FileRecv\0823标注数量统计.xlsx"
mark_detail = pd.read_excel(mark_detail_path)

for j in range(team_num):
    img_num = 0
    err_num = 0
    for i in range(len(mark_detail)):
        for name in team_list[j]:
            if mark_detail['标注员名字'][i] == name:
                img_num += mark_detail['领取任务数'][i]
                err_num += mark_detail['驳回未标注数量'][i]
    team_list[j].append("领取任务数:")
    team_list[j].append(img_num)
    team_list[j].append("驳回未标注数量:")
    team_list[j].append(err_num)

for i in range(team_num):
    people_num = team_list[i][2]
    img_num = people_num * 67  # 应当领取的图片数
    real_img_num = team_list[i][-3]  # 领取任务数
    err_num = team_list[i][-1]  # 驳回数
    should_complete = 0  # 应完成
    if real_img_num > img_num:
        pass_rate = (real_img_num - err_num) / img_num
        should_complete = round(real_img_num * 0.95)
    else:
        pass_rate = (real_img_num - err_num) / real_img_num
        should_complete = round(img_num * 0.95)
    if pass_rate > 0.95:
        mark_score = 10
    else:
        if pass_rate < 0.9:
            mark_score = 0
        else:
            mark_score = 8
    if pass_rate > 1:
        pass_rate = 1
    team_list[i].append("标注得分")
    team_list[i].append(mark_score)
    team_list[i].append(should_complete)
    team_list[i].append(pass_rate)

csv_file = open('mark_score.csv', 'w', newline='')  # encoding='utf-8'
writer = csv.writer(csv_file, delimiter=",")
header = ["队名", "队长名", "手机号", "标注得分", "队伍应领取", "实际领取", "应完成", "实际完成", "通过率"]
writer.writerow(header)

for i in range(team_num):
    csv_row = [team_list[i][1], team_list[i][3], team_list[i][4], team_list[i][-3],
               team_list[i][2]*67, team_list[i][-7], team_list[i][-2],
               team_list[i][-7] - team_list[i][-5], '{:.2%}'.format(team_list[i][-1])]
    writer.writerow(csv_row)
csv_file.close()
