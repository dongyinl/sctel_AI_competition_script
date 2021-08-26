import os
import cv2 as cv

# 不能有中文
dir_path = r'G:\100'
files = os.listdir(dir_path)
print(files)
for file in files:
    img = cv.imread(dir_path + '/' + file)
    img = cv.resize(img, dsize=(900, 1200))
    cv.imwrite(dir_path + '/' + file, img)
