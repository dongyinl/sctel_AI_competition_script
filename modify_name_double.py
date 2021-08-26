import os,sys

file_path_2 = r'G:\桌面暂存\CT\race2021\data\B\100\origin\2'

last_num = 1244
count = begin = last_num*2

for files in os.listdir(file_path_2):
    Olddir=os.path.join(file_path_2,files)
    if os.path.isdir(Olddir):
        continue
    if count%2 == 0:
        # Newdir=os.path.join(file_path_2,"no_title_double"+str(count//2+int(1))+".jpg")
        Newdir=os.path.join(file_path_2, str(count//2+int(1))+".jpg")
        os.rename(Olddir,Newdir)
    else:
        # Newdir=os.path.join(file_path_2,"no_title_double"+str(count//2+int(1))+"-1.jpg")
        Newdir=os.path.join(file_path_2, str(count//2+int(1))+"-1.jpg")
        os.rename(Olddir,Newdir)
    count += 1
print("一共修改了"+str(count-begin)+"个文件")
print(count//2)