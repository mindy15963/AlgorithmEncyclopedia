# 세마포어(Semaphore)
# 정수값을 갖는 변수이며 자원의 개수를 의미한다.

import threading

t=int(input('쓰레드의 개수 입력 : '))
sp=int(input('제한할 쓰레드의 개수 입력 : '))
r=int(input('반복 작업할 횟수 입력 : '))

sem = threading.Semaphore(sp)

class RestrictedArea(threading.Thread):
        def run(self):
                for x in range(r):
                        msg = '쓰레딩 세마포어 테스트 : %s' % self.getName()
                        sem.acquire()
                        print(msg)
                        sem.release()

threads = []

for i in range(t):
        threads.append(RestrictedArea())

for th in threads:
        th.start()

for th in threads:
        th.join()

print('모든 쓰레드가 종료되었습니다.')