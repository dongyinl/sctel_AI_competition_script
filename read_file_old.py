# -*- coding: gbk -*-
import os

path = r'G:\�����ݴ�\CT\race2021\data\B'
folder = os.listdir(path)
lines = []

dir_name = ['111', '000', '110', '100']
for filename in folder:
    lines.append(filename)

f = open("tmp_test.csv", "a")  # rֻ����w��д��a׷��
for line in lines:
    if line[-6:-4] != '-1':
        f.write(line+'\n')
f.close()
