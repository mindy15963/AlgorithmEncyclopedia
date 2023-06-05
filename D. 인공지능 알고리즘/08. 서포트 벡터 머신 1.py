# 서포트 벡터 머신 (Support Vector Machine, SVM)
# 패턴 인식, 자료 분석을 위한 지도 학습 모델으로 주로 분류와 회귀 분석을 위해 사용한다.
# 이 코드는 분류 서포트 벡터 머신에 대해 다룬다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

dc=int(input('데이터의 개수 입력 : '))
rs=int(input('랜덤 상태 입력 : '))
x, y = make_blobs(n_samples=dc, centers=2, random_state=rs)

ko=input('원하는 옵션 입력 (linear, poly, rbf, sigmoid, precomputed): ')
clf = svm.SVC(kernel=ko)
clf.fit(x, y)

newData = [list(input('데이터 입력 : ').split())]
print('예측값 : ',clf.predict(newData))

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title("분류 서포트 벡터 머신")
plt.scatter(x[:,0], x[:,1], c=y, s=30, cmap=plt.cm.Paired)

ax = plt.gca()

xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--', '-', '--'])

ax.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=60, facecolors='r')
plt.show()

if ko=='linear':
    print('가중치 : ',clf.coef_)
print('절편향 : ',clf.intercept_)
print('학습 정확도 : ',np.mean(y==clf.predict(x)))