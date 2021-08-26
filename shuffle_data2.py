import os
import pandas as pd
import cv2 as cv
import shutil
# srcfile = "C:\\Users\\E\\Desktop\\BBB.xlsx"
# dstpath = "C:\\Users\\E\\Desktop\\BBY.xlsx"
# shutil.copy(srcfile, dstpath)



f_pd = pd.read_csv('E:\\AA\\A榜.csv')


def modify_file_name(old_path, name, n):
    for item in os.listdir(old_path):
        if name == item[:-4]:
            srcfile=os.path.join(old_path, item)
            print("srcfile is",srcfile)
            new_name = str(n)
            dstpath = "E:\\AA\\B\\%s.jpg"%new_name
            print("dstpath is", dstpath)
            shutil.copy(srcfile, dstpath)
        print(name+"-1")
        if (name+"-1")== item[:-4]:
                srcfile = os.path.join(old_path, item)
                print("srcfile is", srcfile)
                new_name = str(n)
                dstpath = "E:\\AA\\B\\%s-1.jpg" % new_name
                print("dstpath is", dstpath)
                shutil.copy(srcfile, dstpath)
            # img = cv.imread(os.path.join(old_path, item))
            # new_name = item.replace(name, str(n))
            # cv.imwrite(old_path + "\\B" + new_name, img)

path = r"E:\\AA"  # 自己改一下路径
n = 1
for file in f_pd['No.']:
    print("file is",file)
    # 拿原始名字，并重新命名文件
#     if file[-6:-4] == '-1':
#         continue
    name = file[:-4]
    modify_file_name(path + "\\A榜-原", name, n)
    file = file.replace(name, str(n))
    f_pd['No.'][n-1] = file
    n += 1
f_pd.to_csv('AA.csv', index=False)