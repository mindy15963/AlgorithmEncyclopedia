# 나이브 베이즈 분류 (Naive Bayes Classification)
# 베이즈 정리를 이용해 만든 확률 분류기의 일종이다.

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_blobs(n_samples=ns, random_state=0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

nb = GaussianNB()
y_pred = nb.fit(x_train, y_train).predict(x_test)
print('정확도 : ',accuracy_score(y_test, y_pred))
print("%d개 중 %d개가 틀렸습니다." % (x_test.shape[0], (y_test != y_pred).sum()))