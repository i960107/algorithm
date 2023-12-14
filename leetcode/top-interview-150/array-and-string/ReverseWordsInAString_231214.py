from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return ' '.join(arr)


s = Solution()
print(s.reverseWords("  hello world  "))
