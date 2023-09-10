from typing import List


class Solution:
    # 주의할점 strs의 길이는 다 다름. [""] 도 가능
    # 글자의 길이 M O(M * N)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for index, (chars) in enumerate(zip(*strs)):
            target = chars[0]
            allSame = True
            for c in chars:
                if c != target:
                    allSame = False
                    break
            if allSame:
                prefix.append(target)
            else:
                break
        return "".join(prefix)

        # 정렬된 결과를 활용 맨 처음과 맨끝이 같다면 가운데도 같다고 볼 수 있음. O(NlogN) list의 길이 N

    def longestCommonPrefix2(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["d", "ra", ""]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["cir", "car"]))
