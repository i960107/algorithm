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
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            # 중복순열이므로 index에 현재의 index넘겨주기
            # list concat한 결과 객체 달라짐!
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


print(solution_two_pointer([2, 3, 6, 7], 7))
print(solution_two_pointer([2, 3, 5], 8))

print(solution([2, 3, 6, 7], 7))
print(solution([2, 3, 5], 8))
