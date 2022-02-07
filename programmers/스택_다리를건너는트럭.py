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

    while end != 0 or bridge_queue[end] != None:
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
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
# 이경우 추가하기!
# print(solution(100, 100, [10]))
