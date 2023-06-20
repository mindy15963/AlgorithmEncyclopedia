# 정규화 (Normalization)
# 서로 다른 피처의 크기를 통일하기 위해 크기를 변환해주는 개념이다.

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

dc=int(input('데이터 개수 입력 : '))

df = pd.DataFrame(np.random.randint(0,100,size=(dc,2)), columns=['x1','x2'])
ms = MinMaxScaler()
df_minmax = ms.fit_transform(df)

print('정규화 결과 : \n',pd.DataFrame(df_minmax, columns = ['x1_minmax', 'x2_minmax']))