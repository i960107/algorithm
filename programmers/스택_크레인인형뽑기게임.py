def solution(board: list, moves: list) -> int:
    answer = 0
    basket = []
    for m in moves:
        # 이중 for문과 zip은 다른 결과!!
        for j in range(len(board)):
            if board[j][m - 1] != 0:
                picked = board[j][m - 1]
                board[j][m - 1] = 0
                if basket and basket[-1] == picked:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(picked)
                break

    return answer


# 테스트케이스로 주어진 예시는 문제에서 설명한 예시일것! 비교해서 배열이 어떻게 인형뽑기를 나타내는지 잘 살피기
# 문제 대충 읽지말고 직접 계산해가며 파악하기
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
