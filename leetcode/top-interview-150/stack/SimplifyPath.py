from typing import List


class Solution:
    # only directories test.txt처럼 파일 이름에 .이 들어가는 경우 없음.
    # ...이 들어갈 수 있음
    # 3단계 너무 깊은데..
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = []
        for c in path:
            if c == "/":
                self.addFileName(stack, ''.join(temp))
                temp = []
            else:
                temp.append(c)

        if temp:
            self.addFileName(stack, ''.join(temp))
        return "/" + "/".join(stack)

    def addFileName(self, stack, filename):
        if not filename:
            return
        if filename == ".":
            return
        elif filename == "..":
            if stack:
                stack.pop()
        else:
            stack.append(filename)


s = Solution()
print(s.simplifyPath("home/foo/../bar/./test"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home"))
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/home//foo"))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../authorized_keys"))
