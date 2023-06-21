# 퍼셉트론 (Perceptron)
# 인공 신경망의 구성 요소로서 다수의 값을 입력받아 하나의 값으로 출력하는 알고리즘이다.

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_blobs(n_samples=ns, random_state=0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

sc = StandardScaler()
sc.fit(x_train)

x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

ppn = Perceptron(max_iter=40, eta0=0.1, random_state=0)
ppn.fit(x_train_std, y_train)
y_pred = ppn.predict(x_test_std)
print('정확도 : ',accuracy_score(y_test, y_pred))