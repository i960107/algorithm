def solution(record: list) -> list:
    d_users = {}
    # 매번 쪼개지 않고 r.split한 결과 배열을 한 변수로 담을 수 있음
    for r in record:
        action = r.split()[0]
        if action == "Enter" or action == "Change":
            uid = r.split()[1]
            nickname = r.split()[2]
            d_users[uid] = nickname

    # append해야함. 닉네임 변경 기록은 출력하지 않기 때문에 record길이보다 짧음
    answer = []
    for r in record:
        action, uid = r.split()[0], r.split()[1]
        if action == "Enter":
            answer.append(d_users[uid] + "님이 " + "들어왔습니다.")
        elif action == "Leave":
            answer.append(d_users[uid] + "님이 " + "나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
