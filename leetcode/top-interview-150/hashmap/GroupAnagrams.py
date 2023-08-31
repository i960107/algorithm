from typing import List
from collections import defaultdict


class Solution:
    # 모든 단어 정렬하는게 100 * 2 = 200
    # O(M * NlogN)
    # 10,000 * 100 * 6 = 6,000,000
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        return [group for key, group in groups.items()]


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
