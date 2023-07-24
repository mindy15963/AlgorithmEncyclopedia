# DENCLUE (DENsity-based CLUstEring)
# 밀도 기반 군집화 알고리즘으로, 데이터 포인트의 밀도를 이용하여 군집을 형성한다.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import warnings
warnings.filterwarnings("ignore")

ns=int(input('표본 데이터의 수 입력 : '))
X, Y = varied = make_blobs(n_samples=ns,cluster_std=[0.8, 0.7, 0.66],random_state=170)
data = pd.DataFrame({
    '특징 1': pd.DataFrame(X)[0],
    '특징 2': pd.DataFrame(X)[1],
    '라벨': Y
})

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(5, 5))
plt.title('DENCLUE 알고리즘')
sns.scatterplot(data=data, x='특징 1', y='특징 2', hue='라벨', palette="deep", s=130)
plt.grid(True)
plt.show()

def kernel_function(X, X_i, h):
    power = np.sqrt(np.square(X-X_i).sum())
    den = 2*h*h
    return np.square((0.399/h))*np.exp(-(power/den))

def gradient_ascent(new_feature, h):
    for i in range(10):
        new_values = [0, 0]
        sum_k = 0
        for j in range(data.shape[0]):
            k = kernel_function(new_feature, data.iloc[j][['특징 1','특징 2']].values, h)
            sum_k += k
            new_values += data.iloc[j][['특징 1','특징 2']].values*k
        new_feature = new_values/sum_k
    return np.round(new_feature,2)

def Denclue(data, h, t):
    data['높이'] = 0.000
    data['new_F1'] = 0.000
    data['new_F2'] = 0.000
    no = 20
    for i in range(data.shape[0]):
        if no==i+1:
            print('*', end="")
            no+=20
        feat_1 = 0
        new_Feature = [0, 0]
        for j in range(data.shape[0]):
            k = kernel_function(data.iloc[i][['특징 1','특징 2']].values, data.iloc[j][['특징 1','특징 2']].values, h)
            feat_1 += k
            new_Feature += data.iloc[j][['특징 1','특징 2']].values*k
        data['높이'][i] = (feat_1/len(data)-t)
        new_Feature /= feat_1
        if data['높이'][i]<0:
            data['높이'][i] = 0
        else:
            g = gradient_ascent(new_Feature, h)
            data['new_F1'][i] = g[0]
            data['new_F2'][i] = g[1]
    centers= pd.DataFrame({
        'F1_center': data[data['new_F1']!=0]['new_F1'].unique(),
        'F2_center': data[data['new_F2']!=0]['new_F2'].unique(),
        '군집': np.arange(1, len(data[data['new_F1']!=0]['new_F1'].unique())+1)
    })
    print('\n\n군집의 중심')
    print(centers)
    data['군집'] = -1
    for i in range(data.shape[0]):
        for j in range(centers.shape[0]):
            if data.iloc[i]['new_F1'] == centers.iloc[j]['F1_center'] and data.iloc[i]['new_F2'] == centers.iloc[j]['F2_center']:
                data['군집'][i] = centers.iloc[j]['군집']
                break
    print('\n각 군집에 데이터 중심점이 없습니다.')
    print(data.groupby('군집')['군집'].count())
    
h = float(input('높이 값 입력 : '))
t = float(input('시간 값 입력 : '))
Denclue(data, h, t)

plt.figure(figsize=(8, 8))
plt.title('DENCLUE 알고리즘')
sns.scatterplot(data=data, x='특징 1', y='특징 2', hue='군집', palette="deep", s=130)
plt.grid(True)
plt.show()

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
  
x = data['특징 1']
y = data['특징 2']
z = data['높이']
  
fig = plt.figure(figsize =(10, 10))
plt.title('DENCLUE 알고리즘')
ax = plt.axes(projection ='3d')
  
ax.plot_trisurf(x, y, z, color="red",
                linewidth = 0,
                antialiased = True , cmap=plt.cm.CMRmap);
plt.xlabel('특징 1')
plt.ylabel('특징 2')
plt.show()