class Solution:
    def isValid(self, s: str):
        if len(s) % 2 == 1:
            return False
        stack = []
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in d:
                stack.append(c)
            else:
                # stack underflow 항상 주의!
                if not stack:
                    return False
                expected = d[stack.pop()]
                if expected != c:
                    return False
        # if stack:
        #     return False
        return not stack


s = Solution()
print(s.isValid("()"))
print(s.isValid("(]"))
print(s.isValid("()]"))
print(s.isValid("((("))
