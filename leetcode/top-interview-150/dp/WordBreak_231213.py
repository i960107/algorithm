from typing import List


class Solution:
    # catsand -> (cats, and) or (cat, sand)
    # 여러가지 경우로 나누어질 수 있음.
    # dfs 로 모든 경로에 대해서 살핀다? -> TLE
    # 한번 체크한 경로 안 체크하도록 visited 체크하기.
    def wordBreak_Fail(self, s: str, wordDict: List[str]):
        path = []
        visited = [False for _ in range(len(s))]

        def dfs(i: int):
            if i == len(s):
                return True

            if visited[i]:
                return False

            visited[i] = True

            for word in wordDict:
                if s[i:i + len(word)] != word:
                    continue
                path.append(word)
                if dfs(i + len(word)):
                    return True
                path.pop()
            return False

        return dfs(0)

    # coin change 에서 응용한 dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 왜 dp[0]을 추가해주는가? -> s = 1)""일때 2)첫번째 단어 체크시 이전 subarray 만족하는 문자열 체크할 수 있도록
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i - len(word) < 0:
                    continue
                if not dp[i - len(word)]:
                    continue
                if s[i - len(word):i] != word:
                    continue
                dp[i] = True
                break
        return dp[len(s)]


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
