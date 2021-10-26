import pandas as pd
import numpy as np

# CSV読み込みと中身の表示
df = pd.read_csv('sample.csv')
print(df)

print('~~~~~~~')

# 行列に行列を追加する
df2 = df.append(df)
print(df2)
