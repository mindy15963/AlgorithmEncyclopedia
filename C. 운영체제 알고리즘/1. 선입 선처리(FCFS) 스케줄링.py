# 선입 선처리(FCFS) 스케줄링
# 먼저 자원 사용을 요청한 프로세스에게 자원을 할당해 주는 방식의 스케줄링 알고리즘이다.

class FCFS:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = input("프로세스 ID 입력: ")
            arrival_time = int(input(f"프로세스 {process_id}의 도착 시간 입력 : "))
            burst_time = int(input(f"프로세스 {process_id}의 실행 시간 입력 : "))
            temporary.extend([process_id, arrival_time, burst_time])
            process_data.append(temporary)
        FCFS.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            if s_time < process_data[i][1]:
                s_time = process_data[i][1]
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)
        t_time = FCFS.calculateTurnaroundTime(self, process_data)
        w_time = FCFS.calculateWaitingTime(self, process_data)
        FCFS.printData(self, process_data, t_time, w_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        print("| 프로세스 ID | 도착 시간 | 실행 시간 | 완료 시간 | 반환 시간 | 대기 시간 |")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end=" |    ")
            print()

        print(f'평균 반환 시간 : {average_turnaround_time}')
        print(f'평균 대기 시간 : {average_waiting_time}')

if __name__ == "__main__":
    no_of_processes = int(input("프로세스의 개수 입력 : "))
    fcfs = FCFS()
    fcfs.processData(no_of_processes)