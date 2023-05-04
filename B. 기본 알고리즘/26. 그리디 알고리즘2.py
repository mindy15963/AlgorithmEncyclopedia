# 그리디(욕심쟁이) 알고리즘 (Greedy Algorithm)
# "매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자"라는 모토를 가지는 알고리즘 설계 기법이다.
# 회의실 배정 문제

n=int(input('신청된 회의 수 입력 : '))

meetings = []

for _ in range(n):
    start, end = map(int, input('회의 시작 시간 및 종료 시간 입력 : ').split(" "))
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print('배정된 회의 수 : ',answer)