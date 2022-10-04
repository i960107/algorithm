from typing import List


def get_char_room_messages(record: List[str]) -> List[str]:
    users = dict()

    for r in record:
        tmp = r.split()

        if tmp[0] == "Change" or tmp[0] == "Enter":
            users[tmp[1]] = tmp[2]

    answer = []
    for r in record:
        tmp = r.split()

        if tmp[0] == "Enter":
            answer.append(users[tmp[1]] + "님이 들어왔습니다.")

        elif tmp[0] == "Leave":
            answer.append(users[tmp[1]] + "님이 들어왔습니다 나갔습니다.")

    return answer


print(get_char_room_messages(["Enter uid1234 Muzi",
                              "Enter uid4567 Prodo",
                              "Leave uid1234",
                              "Enter uid1234 Prodo",
                              "Change uid4567 Ryan"]))
