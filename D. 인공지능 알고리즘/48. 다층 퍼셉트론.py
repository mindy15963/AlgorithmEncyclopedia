# 다층 퍼셉트론 (Multilayer Perceptron, MLP)
# 여러 개의 은닉층을 갖는 퍼셉트론이다.

import torch
import torch.nn as nn
device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)
    
X = torch.FloatTensor([[0, 0], [0, 1], [1, 0], [1, 1]]).to(device)
Y = torch.FloatTensor([[0], [1], [1], [0]]).to(device)

hl=int(input('은닉층 개수 입력 : '))

modules = []
modules.append(nn.Linear(2, 10, bias=True))
modules.append(nn.Sigmoid())
for i in range(hl-1):
    modules.append(nn.Linear(10, 10, bias=True))
    modules.append(nn.Sigmoid())
modules.append(nn.Linear(10, 1, bias=True))
modules.append(nn.Sigmoid())

model = nn.Sequential(*modules).to(device)

criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=1)

ep=int(input('에포크 횟수 입력 : '))

for epoch in range(ep): 
    optimizer.zero_grad()
    hypothesis = model(X)

    cost = criterion(hypothesis, Y)
    cost.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print(epoch, cost.item())
        
with torch.no_grad():
    hypothesis = model(X)
    predicted = (hypothesis > 0.5).float()
    accuracy = (predicted == Y).float().mean()
    print('모델의 출력값 : ', hypothesis.detach().cpu().numpy())
    print('모델의 예측값 : ', predicted.detach().cpu().numpy())
    print('실제값 : ', Y.cpu().numpy())
    print('정확도 : ', accuracy.item())