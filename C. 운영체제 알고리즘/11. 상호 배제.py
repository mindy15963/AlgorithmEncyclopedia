# 상호 배제 (Mutex)
# 동시 프로그래밍에서 공유 불가능한 자원의 동시 사용을 피하기 위해 사용되는 알고리즘으로, 임계 구역으로 불리는 코드 영역에 의해 구현된다.

import threading, time, random
 
mutex = threading.Lock()
class thread_one(threading.Thread):
	def run(self):
		global mutex
		print("첫번째 쓰레드가 대기하고 있습니다.")
		time.sleep(random.randint(1, 5))
		print("첫번째 쓰레드가 종료되었습니다.")
		mutex.release()
 
class thread_two(threading.Thread):
	def run(self):
		global mutex
		print("두번째 쓰레드가 대기하고 있습니다.")
		time.sleep(random.randint(1, 5))
		mutex.acquire()
		print("두번째 쓰레드가 종료되었습니다.")
  
mutex.acquire()
t1 = thread_one()
t2 = thread_two()
t1.start()
t2.start()