# 최상 응답 비율 순서(HRN, HRRN) 스케줄링
# 프로세스 처리의 우선 순위를 CPU 처리 기간과 해당 프로세스의 대기 시간을 동시에 고려해 선정하는 스케줄링 알고리즘이다.

class HRRN:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("프로세스 ID 입력: "))
            arrival_time = int(input(f"프로세스 {process_id}의 도착 시간 입력 : "))
            burst_time = int(input(f"프로세스 {process_id}의 실행 시간 입력 : "))
            temporary.extend([process_id, arrival_time, burst_time, 0])
            process_data.append(temporary)
        HRRN.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_processes = []
        process_data.sort(key=lambda x: x[1])
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    response_ratio = 0
                    response_ratio = float(((s_time - process_data[j][1]) + process_data[j][2]) / process_data[j][2])
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], response_ratio])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        t_time = HRRN.calculateTurnaroundTime(self, process_data)
        w_time = HRRN.calculateWaitingTime(self, process_data)
        HRRN.printData(self, process_data, t_time, w_time, sequence_of_processes)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_processes):
        process_data.sort(key=lambda x: x[0])
        print("| 프로세스 ID | 도착 시간 | 실행 시간 | 실행 완료 | 완료 시간 | 반환 시간 | 대기 시간 |")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="\t\t\t\t")
            print()
        print(f'평균 반환 시간 : {average_turnaround_time}')
        print(f'평균 대기 시간 : {average_waiting_time}')
        print(f'프로세스의 시퀀스: {sequence_of_processes}')

if __name__ == "__main__":
    no_of_processes = int(input("프로세스의 개수 입력 : "))
    hrrn = HRRN()
    hrrn.processData(no_of_processes)