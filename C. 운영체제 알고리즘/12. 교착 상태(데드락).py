# 교착 상태(Deadlock)
# 운영체제 또는 소프트웨어의 잘못된 자원 관리로 인하여 둘 이상의 프로세스 또는 스레드들이 아무것도 진행하지 않는 상태로 서로 영원히 대기하는 상황으로, 멀티스레딩, 병렬 프로그래밍, 분산 컴퓨팅에서 흔히 발생하는 문제이다.

import logging
from concurrent.futures import ThreadPoolExecutor
import time
import string as s

class Banko:
    def __init__(self):
        self.money = 0
        
    def deposit_1000won(self, user_name):
        print("Thread {}: 입금 시작합니다.".format(user_name))
        
        local_data = self.money
        local_data += 1000 
        time.sleep(0.1)
        self.money = local_data
        
        print("Thread {}: 입금 종료합니다.".format(user_name))

if __name__ == "__main__":
    bank = Banko()
    n=int(input('고객 수 입력 : '))
    
    print("은행 계좌를 생성하였습니다. 현재 잔액: {}원".format(bank.money))
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        for user_name in s.ascii_uppercase[:n]:
            executor.submit(bank.deposit_1000won, user_name)
            
    print("은행 계좌 현재 잔액: {}원".format(bank.money))