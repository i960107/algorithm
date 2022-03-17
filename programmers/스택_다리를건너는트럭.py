from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    sec = 0

    # bridge를 환형 큐로 표현.한바퀴돌고 오면 그 트럭은 다리를 다 지난것
    end = -1

    bridge_queue = [None] * bridge_length
    waiting_truck_index = 0
    weight_on_bridge = 0
    while True:
        sec += 1
        end = (end + 1) % bridge_length
        if bridge_queue[end]:
            weight_on_bridge -= bridge_queue[end]
            # 다리 건넌 트럭 처리
            bridge_queue[end] = None

        # print(f'{sec}초 남은 하중 {weight - weight_on_bridge} 기다리는 트럭 무게 {truck_weights[waiting_truck_index]}')
        # 무게 맞으면 추가
        if truck_weights[waiting_truck_index] <= weight - weight_on_bridge:
            bridge_queue[end] = truck_weights[waiting_truck_index]
            weight_on_bridge += truck_weights[waiting_truck_index]
            waiting_truck_index += 1

        # 왜 결과가 다르게 나오지
        # if waiting_truck_index >= len(truck_weights) - 1:
        if waiting_truck_index > len(truck_weights) - 1:
            break

    while end != 0 or bridge_queue[end]:
        if bridge_queue[end]:
            weight_on_bridge -= bridge_queue[end]
            # 다리 건넌 트럭 처리
            bridge_queue[end] = None
        end = (end + 1) % bridge_length
        sec += 1

    return sec

    # time[0] = 0
    # for i in range(0, len(truck_weights)):
    #     weight_on_bridge = 0
    #     for j in range(i - bridge_length, i):
    #         if time[i - j] < bridge_length:
    #             time[i - j] += 1
    #             weight_on_bridge += truck_weights[i - j]
    #     if weight - weight_on_bridge >= truck_weights[i]:
    #         time[i] += 1
    #


def solution2(bridge_length: int, weight: int, truck_weights: list) -> int:
    sec = 0

    # 다리를 다 건넜다는것 추가해주기 위해 +1
    bridge = [None] * (bridge_length + 1)
    weight_on_bridge = 0
    # 0이 다리의 끝 -> 트럭이 삽입되는 곳, 배열의 끝이 다리의 처음 -> 트럭이 삭제되는 곳
    # bridge_rear처음에 무효한 값?
    # bridge_rear을 기준으로 bridge_front 값 구하기?
    bridge_rear = -1
    # 초기 값 -1 ?
    bridge_front = -1

    truck_waiting = 0

    truck_done = []

    while True:
        sec += 1

        # front, rear 포인터 조정 어디서?
        # bridge_rear에 값 삽입해야함. rear는 배열의 마지막이 되어야함.
        # 포인터 조정 후 값 삽입, 값 삽입 후 포인터 조정 어떻게 다르지?
        # i_circular_queues 와 어떻게 다르지? 값이 몇개이든 상관없이 front 와 rear의 차이 즉 다리의 길이가 유지되어야
        bridge_front = (bridge_front + 1) % bridge_length
        bridge_rear = (bridge_front + bridge_length) % bridge_length

        # 다리 끝에 도착한 트럭 다리에서 내리기
        if bridge[bridge_front]:
            weight_on_bridge -= bridge[bridge_front]
            truck_done.append(bridge[bridge_front])
        bridge[bridge_front] = None

        # 대기열에 있는 트럭 무게 맞으면 다리에 올리기
        if truck_waiting <= len(truck_weights) - 1 and truck_weights[truck_waiting] <= weight - weight_on_bridge:
            bridge[bridge_rear] = truck_weights[truck_waiting]
            weight_on_bridge += truck_weights[truck_waiting]
            truck_waiting += 1

        if len(truck_done) == len(truck_weights):
            break

    return sec


def solution_deque(bridge_length: int, weight: int, truck_weights: list) -> int:
    '''deque을 활용한 풀이'''
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    # pop()하는 시간 줄이기 위해 reverse 복잡도 O(n)
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)
        step += 1

    step += bridge_length
    return step


def solution_test(bridge_length: int, weight: int, truck_weights: list) -> int:
    sec = 0
    bridge = [0] * bridge_length
    bridge_front = 0
    bridge_rear = bridge_length - 1
    truck_index = 0
    # 시간이 오래 걸리는 이유는 sum() 때문 -> 무게를 추적하고 있는게 더 나음!!

    while True:
        sec += 1

        # 다리 앞에 도착해서 내린 트럭 조정
        bridge[bridge_front] = 0
        bridge_front = (bridge_front + 1) % bridge_length

        # 다리 끝에 올라가는 트럭 조정
        bridge_rear = (bridge_rear + 1) % bridge_length
        if weight - sum(bridge) >= truck_weights[truck_index]:
            bridge[bridge_rear] = truck_weights[truck_index]
            truck_index += 1

        # 더 이상 기다리는 트럭이 없을때 (모든 트럭이 다리를 건너거나 다리 위에 있음)
        if truck_index > len(truck_weights) - 1:
            break

    sec += bridge_length

    return sec


print(solution_test(2, 10, [7, 4, 5, 6]))
print(solution_test(100, 100, [10]))
print(solution_test(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
