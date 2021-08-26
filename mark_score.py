# -*- coding: gbk -*-
import csv
import pandas as pd

signup_path = r"D:\doc\2358951845\FileRecv\2021���Ĵ�����AI�Ͷ�����������Ϣ.xlsx"
signup = pd.read_excel(signup_path)
signup = pd.read_excel(signup_path)

team_num = len(signup)
team_list = []
# team_list: [[..], [..], [..]]
for i in range(team_num):
    tmp_list = []
    if isinstance(signup["��Ա4����"][i], str):
        tmp_list = [i + 1, signup["�Ŷ�����"][i], 5, signup["�ӳ�����"][i], signup["�ӳ��绰"][i],
                    signup["��Ա1����"][i], signup["��Ա2����"][i], signup["��Ա3����"][i], signup["��Ա4����"][i]]
    else:
        if isinstance(signup["��Ա3����"][i], str):
            tmp_list = [i + 1, signup["�Ŷ�����"][i], 4, signup["�ӳ�����"][i], signup["�ӳ��绰"][i],
                        signup["��Ա1����"][i], signup["��Ա2����"][i], signup["��Ա3����"][i]]
        else:
            tmp_list = [i + 1, signup["�Ŷ�����"][i], 3, signup["�ӳ�����"][i], signup["�ӳ��绰"][i],
                        signup["��Ա1����"][i], signup["��Ա2����"][i]]
    team_list.append(tmp_list)

mark_detail_path = r"D:\doc\2358951845\FileRecv\0823��ע����ͳ��.xlsx"
mark_detail = pd.read_excel(mark_detail_path)

for j in range(team_num):
    img_num = 0
    err_num = 0
    for i in range(len(mark_detail)):
        for name in team_list[j]:
            if mark_detail['��עԱ����'][i] == name:
                img_num += mark_detail['��ȡ������'][i]
                err_num += mark_detail['����δ��ע����'][i]
    team_list[j].append("��ȡ������:")
    team_list[j].append(img_num)
    team_list[j].append("����δ��ע����:")
    team_list[j].append(err_num)

for i in range(team_num):
    people_num = team_list[i][2]
    img_num = people_num * 67  # Ӧ����ȡ��ͼƬ��
    real_img_num = team_list[i][-3]  # ��ȡ������
    err_num = team_list[i][-1]  # ������
    should_complete = 0  # Ӧ���
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
    team_list[i].append("��ע�÷�")
    team_list[i].append(mark_score)
    team_list[i].append(should_complete)
    team_list[i].append(pass_rate)

csv_file = open('mark_score.csv', 'w', newline='')  # encoding='utf-8'
writer = csv.writer(csv_file, delimiter=",")
header = ["����", "�ӳ���", "�ֻ���", "��ע�÷�", "����Ӧ��ȡ", "ʵ����ȡ", "Ӧ���", "ʵ�����", "ͨ����"]
writer.writerow(header)

for i in range(team_num):
    csv_row = [team_list[i][1], team_list[i][3], team_list[i][4], team_list[i][-3],
               team_list[i][2]*67, team_list[i][-7], team_list[i][-2],
               team_list[i][-7] - team_list[i][-5], '{:.2%}'.format(team_list[i][-1])]
    writer.writerow(csv_row)
csv_file.close()
