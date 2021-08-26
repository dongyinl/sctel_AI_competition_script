# -*- coding: gbk -*-
import os
import csv

path = r'G:\桌面暂存\CT\race2021\data\B'  # 自己改好数据文件的路径
dir_name = ['111', '000', '110', '100']
csv_file = open(os.path.join(path, 'B_order.csv'), 'a', newline='')  # encoding='utf-8'
writer = csv.writer(csv_file, delimiter=",")
header = ["No.", "logo", "tel", "sign"]
writer.writerow(header)

for i in range(len(dir_name)):
    dir_path = os.path.join(path, dir_name[i])
    folder = os.listdir(dir_path)
    for filename in folder:
        if filename[-6:-4] != '-1':
            csv_row = [filename, dir_name[i][0], dir_name[i][1], dir_name[i][2]]
            writer.writerow(csv_row)

csv_file.close()

# # create csv pandas做csv的标题太麻烦了，而且还不好用
# title_label = pd.DataFrame(index=None, columns=["logo", "tel", "sign"])
# title_label.to_csv(os.path.join(path, 'temp.csv'))
# temp_csv = pd.read_csv(os.path.join(path, 'temp.csv'))
# temp_csv.columns = ["No."] + temp_csv.columns[1:].tolist()
# temp_csv.to_csv(os.path.join(path, 'B.csv'), index=False)
