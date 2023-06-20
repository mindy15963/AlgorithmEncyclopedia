# 표준화 (Standardization)
# 데이터의 피처 각각이 평균이 0이고 분산이 1인 가우시안 정규분포를 가진 값으로 변환하는 것을 의미한다.

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

dc=int(input('데이터 개수 입력 : '))

df = pd.DataFrame(np.random.randint(0,100,size=(dc,2)), columns=['x1','x2'])
ss = StandardScaler()
df_std = ss.fit_transform(df)

print('표준화 결과 : \n',pd.DataFrame(df_std, columns = ['x1_std', 'x2_std']))