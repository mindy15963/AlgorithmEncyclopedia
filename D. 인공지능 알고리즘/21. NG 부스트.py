# NG 부스트 (NG Boost)
# 확률론적 예측을 위한 자연 그래디언트 부스팅이다.

from sklearn.model_selection import train_test_split
from ngboost import NGBClassifier
from ngboost.distns import Bernoulli
from sklearn.datasets import make_moons
from sklearn.metrics import roc_auc_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

ngb = NGBClassifier(Dist=Bernoulli)
ngb.fit(x_train, y_train)

preds = ngb.pred_dist(x_test)
print("ROC : ", roc_auc_score(y_test, preds.probs[1]))