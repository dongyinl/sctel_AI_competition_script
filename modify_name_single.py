import os,sys
file_path_1 = r'G:\桌面暂存\CT\race2021\data\B\100\origin\1'

count = begin = 1205

for files in os.listdir(file_path_1):
    Olddir=os.path.join(file_path_1,files)
    if os.path.isdir(Olddir):
        continue
    Newdir=os.path.join(file_path_1,str(count+int(1))+".jpg")
    os.rename(Olddir,Newdir)
    count+=1
print("一共修改了"+str(count-begin)+"个文件")
print(count)