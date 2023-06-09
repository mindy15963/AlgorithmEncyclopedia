# 주성분 분석 (Principal Component Analysis, PCA)
# 원 데이터의 분포를 최대한 보존하면서 고차원 공간의 데이터들을 저차원 공간으로 변환하는 기법이다.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA

dc=int(input('데이터의 개수 입력 : '))
nc=int(input('요소의 개수 입력 : '))
ci = [input('요소 항목 입력 : ') for _ in range(nc)]

x, y = make_blobs(n_samples=dc, n_features=nc, centers=4, random_state=4)

pca = PCA(n_components=nc).fit(x)

print(f'성분 벡터 : \n{pca.components_}')
 
print('데이터 총 분산 : ', np.sum(np.diag(pca.get_covariance())))
print('주성분의 분산 : ', pca.explained_variance_)
print('분산 설명 비율 : ', pca.explained_variance_ratio_)

pc = pca.transform(x)
print('주성분 : \n',pc)

inverse_pc = pca.inverse_transform(pc)
print('원 데이터 : \n',inverse_pc)

pc_df = pd.DataFrame(data = pc,columns = ci)
pc_df['Cluster'] = y
pc_df.head()

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title("주성분 분석")
df = pd.DataFrame({'분산':pca.explained_variance_ratio_,'요소':ci})
sns.barplot(x='요소',y="분산",data=df, color="c")

i1, i2 = input("측정할 요소 항목 입력 : ").split()

sns.lmplot( x=i1, y=i2,
  data=pc_df, 
  fit_reg=False, 
  hue='Cluster',
  legend=True,
  scatter_kws={"s": 80})
plt.show()