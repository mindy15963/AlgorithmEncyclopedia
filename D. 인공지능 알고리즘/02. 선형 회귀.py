# 선형 회귀 (Linear Regression)
# 알려진 다른 관련 데이터 값을 사용하여 알 수 없는 데이터의 값을 예측하는 데이터 분석 기법이다.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dc=int(input('데이터의 개수 입력 : '))
mx=int(input('x 값의 최대값 입력 : '))
data_set=[]
y_list=[]
for i in range(dc):
    x_val=np.random.randint(1,mx)
    mul=np.random.uniform(0.7,1.2)
    y_val=x_val*mul
    data_set.append([x_val,y_val])

df=pd.DataFrame(data_set,columns=['x 값','y 값'])
print(df)

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

L_reg=LinearRegression()
L_reg.fit(x,y)
y_pre=L_reg.predict(x)

plt.rcParams['font.family']='Malgun Gothic'
plt.title('선형 회귀')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.scatter(x,y)
plt.plot(x,y_pre,color='red')
plt.show()