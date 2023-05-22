# 최소 잔류 시간 우선(SRT, SRTF) 스케줄링
# SJF 스케줄링을 비선점에서 선점 형태로 수정한 스케줄링 알고리즘으로 현재 작업 중인 프로세스를 중단시키고 새로 들어온 프로세스의 처리를 시작하는 방식이다.

class SRT:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = input("프로세스 ID 입력: ")
            arrival_time = int(input(f"프로세스 {process_id}의 도착 시간 입력 : "))
            burst_time = int(input(f"프로세스 {process_id}의 실행 시간 입력 : "))
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
        SRT.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
        t_time = SRT.calculateTurnaroundTime(self, process_data)
        w_time = SRT.calculateWaitingTime(self, process_data)
        SRT.printData(self, process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])
        print("| 프로세스 ID | 도착 시간 | 남은 실행 시간 | 실행 완료 | 원래 실행 시간 | 완료 시간 | 반환 시간 | 대기 시간 |")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end=" |    ")
            print()
        print(f'평균 반환 시간 : {average_turnaround_time}')
        print(f'평균 대기 시간 : {average_waiting_time}')
        print(f'프로세스의 순서 : {sequence_of_process}')

if __name__ == "__main__":
    no_of_processes = int(input("프로세스의 개수 입력 : "))
    srt = SRT()
    srt.processData(no_of_processes)