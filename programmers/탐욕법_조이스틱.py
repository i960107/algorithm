def solution(name: str) -> int:
    a = ord('A')
    z = ord('Z')
    # 알파벳 변경하는 횟수
    change = [min(ord(c) - a, z - ord(c) + 1) for c in name]

    # 진행 방향
    direction = {"right": 1, "left": -1}
    # 커서 이동하는 횟수
    # A가 중간에서 연속되게 나올경우
    i, answer = 0, 0
    while True:
        answer += change[i]
        change[i] = 0

        if sum(change) == 0:
            break
        left, right = 1, 1
        # 좌우 방향 전환 시에는 바꿔야 하는 알파벳이 나오기까지의 좌우거리를 구한 뒤, 그 중 최솟값이 되는 방향을 전환
        # 바로 다음 알파벳까지의 거리만 구하면 되나?
        while change[i - left] == 0:
            left += 1
        while change[i + right] == 0:
            right += 1
        answer += left if left < right else right
        i += - left if left < right else right
    return answer


print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
