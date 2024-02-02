from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitLetterMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        answer = []
        path = []

        def dfs(pos: int):
            if pos == len(digits):
                answer.append(''.join(path))
                return
            for num in digitLetterMap[digits[pos]]:
                path.append(num)
                dfs(pos + 1)
                path.pop()

        dfs(0)
        return answer


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))  # 빈배열과, 빈문자열을 원소로 가지는 배열은 다름!
print(s.letterCombinations("2"))
