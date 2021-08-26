import pandas as pd
A_data = pd.read_csv("A_rand.csv")

modify_list = [14, 377]

for i in modify_list:
    # 自己更改需要的数字
    A_data['logo'][i-1] = 1
    A_data['tel'][i-1] = 1
    A_data['sign'][i-1] = 1

# print(A_data['sign'][62])
A_data.to_csv("A_rand.csv", index=False)
