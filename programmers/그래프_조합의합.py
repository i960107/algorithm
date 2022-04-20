from typing import List


def solution_two_pointer(candidates: List[int], target: int) -> List[List[int]]:
    # 몇개의 수를 활용할 수 있는지 나와있지 않으므로 two pointer활용 불가
    answer = []
    l, u = 0, len(candidates) - 1
    while l < u:
        curr = candidates[l] + candidates[u]
        if curr > target:
            u -= 1
        elif curr < target:
            l += 1
        else:
            answer.append([l, u])
            break
    return answer

    # def solution(candidates: List[int], target: int) -> List[List[int]]:
    #     result = []
    #
    #     def dfs(csum: int, index: int, path: List[int]):
    #
    #         if csum > target:
    #             return
    #         if csum == target:
    #             result.append(path[:])
    #             return
    #
    #         for i in range(index, len(candidates)):
    #             path.append(candidates[i])
    #             csum += candidates[i]
    #             dfs(csum, index + 1, path)
    #             path.pop()
    #
    #     dfs(0, 0, [])
    #     return result


def solution(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum: int, index: int, path: List[int]):
        # sum을 넘기거나, 남은 값을 넘기거나
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            # 중복순열이므로 index에 현재의 index넘겨주기
            # list concat한 결과 객체 달라짐!
            # int형은 참조아니기때문에 csum -= candidates[i]후 넘겨줘도 되나? 아님!
            # 값이 누적됨 왜? csum은 global변수이기 때문에 같은 level의 호출된 함수에서 값을 공유함
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


def solution_test(candidates: List[int], target: int) -> List[List[int]]:
    answer = []

    def dfs(index: int, csum: int, path: List[int]):
        if csum == target:
            answer.append(path)
            return
        if csum > target:
            return
        for i in range(index, len(candidates)):
            new_csum = csum + candidates[i]
            dfs(i, new_csum, path + [candidates[i]])

    dfs(0, 0, [])
    return answer


print(solution([2, 3, 6, 7], 7))
print(solution([2, 3, 5], 8))
print(solution_test([2, 3, 6, 7], 7))
print(solution_test([2, 3, 5], 8))
