# 메모리 네트워크(Memory Network)
# 장기적인 기억을 처리하기 위한 구조를 가진 인공 신경망이다.

import torch
import torch.nn as nn

memory_size = 10
embedding_size = 20
memory = torch.zeros(memory_size, embedding_size)

def get_embedding(input_data):
    embedding = torch.zeros(embedding_size)
    embedding[input_data] = 1
    return embedding

train_input = int(input('입력할 값 입력 : '))
to = list(map(float, input('출력할 값 입력 : ').split()))
train_output = torch.tensor(to)

embedding = get_embedding(train_input)
memory[train_input] = embedding

def predict(input_data):
    embedding = get_embedding(input_data)
    distances = torch.norm(memory - embedding, dim=1)
    nearest_idx = torch.argmin(distances)
    return memory[nearest_idx]

prediction = predict(train_input)
print("예측 : \n", prediction)