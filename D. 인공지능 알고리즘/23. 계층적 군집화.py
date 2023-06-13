# 계층적 군집화 (Hierarchical Clustering)
# 데이터를 계층적으로 연결해가면서 유사도가 높거나 가까운 군집끼리 군집을 구성해 가는 알고리즘이다.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import *

ns=int(input('표본 데이터의 수 입력 : '))

X=np.random.randint(0,100,size=(ns,2))

linked = linkage(X, 'single')

labelList = range(1, ns+1)

plt.rcParams['font.family']='Malgun Gothic'
plt.figure(figsize=(10, 7))
plt.title("계층적 군집화")
dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)
plt.show()