# 정규화 (Normalization)
# 서로 다른 피처의 크기를 통일하기 위해 크기를 변환해주는 개념이다.

import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler

dc=int(input('데이터 개수 입력 : '))

df = pd.DataFrame(np.random.randint(0,100,size=(dc,2)), columns=['x1','x2'])
rs = RobustScaler()
df_robust = rs.fit_transform(df)

print('정규화 결과 : \n',pd.DataFrame(df_robust, columns = ['x1_robust', 'x2_robust']))