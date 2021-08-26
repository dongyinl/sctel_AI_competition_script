import os
import pandas as pd
import cv2 as cv

f_pd = pd.read_csv('A榜-原.csv')


def modify_file_name(old_path, name, n):
    for item in os.listdir(old_path):
        if name == item[:-4]:  # ('-')
            img = cv.imread(os.path.join(old_path, item))
            new_name = str(n) + '.jpg'
            cv.imwrite(old_path + "/../A/" + new_name, img)
        if (name + '-1') == item[:-4]:
            img = cv.imread(os.path.join(old_path, item))
            new_name = str(n) + '-1.jpg'
            cv.imwrite(old_path + "/../A/" + new_name, img)


path = r""  # 自己改一下路径
n = 1
for file in f_pd['No.']:
    # 拿原始名字，并重新命名文件
    #     if file[-6:-4] == '-1':
    #         continue
    name = file[:-4]
    modify_file_name(path + "/A榜-原", name, n)
    file = file.replace(name, str(n))
    f_pd['No.'][n - 1] = file
    n += 1
f_pd.to_csv('A.csv', index=False)
