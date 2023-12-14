from typing import List


class Solution:
    # trie를 사용해서 가지가 갈라지지 않을때까지. -> 모든 글자에게 대해 trie를 만드는 작업이 필요함.
    # brute force로 될거 같은데.
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = []
        i = 0
        while True:
            if i >= len(v[0]):
                break
            prefix = v[0][i]
            unsatisfied = False
            for j in range(1, len(v)):
                if i >= len(v[j]) or v[j][i] != prefix:
                    unsatisfied = True
                    break
            if unsatisfied:
                break
            ans.append(prefix)
            i += 1
        return ''.join(ans)


s = Solution()
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
