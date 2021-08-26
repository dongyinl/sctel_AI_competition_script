import pandas as pd
from sklearn.utils import shuffle

data = pd.read_csv('A.csv', encoding='unicode_escape')
data = shuffle(data)  # 打乱
data.to_csv('A榜.csv')
# 然后再用shuffle_data2.py处理
