class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False


# 빈 문자열은 입력으로 주어지지 않는다.
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    # .은 글자 하나를 의미하는 와일드카드이다.
    # 스택을 사용한 dfs, 재귀 dfs, bsf 다 가능.
    # 왜 재귀 dsf가 더 빠르지?
    # dfs bfs중 뭐가 나을까?
    def search1(self, word: str) -> bool:

        stack = [(self.root, 0)]
        found = False
        while not found and stack:
            curr, index = stack.pop()
            if index == len(word):
                if curr.isEndOfWord:
                    found = True
                continue

            c = word[index]
            if c == ".":
                for child in curr.children:
                    stack.append((curr.children[child], index + 1))
            elif c in curr.children:
                nxt = curr.children[c]
                stack.append((nxt, index + 1))
        return found


class WordDictionary2:
    # TrieNode 구현하지 않고 dict() + EOW 사용
    def __init__(self):
        self.root = dict()
        self.EOW = "EOW"
        self.root[self.EOW] = False

    # 소문자만 저장됨. EOW와 일치하는 글자 저장될 일 없음
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = dict()
                curr[c][self.EOW] = False
            curr = curr[c]
        curr[self.EOW] = True

    # .은 글자 하나를 의미하는 와일드카드이다.
    # 스택을 사용한 dfs, 재귀 dfs, bsf 다 가능.
    # 문자 개수가 많아질수록 iterative 버전이 나을듯.
    # 왜 재귀 dsf가 더 빠르지?
    # 백트래킹 bfs시 큐 크기가 너무 커질 수 있음
    # dfs bfs중 뭐가 나을까?
    def search(self, word: str) -> bool:

        stack = [(self.root, 0)]
        found = False
        while not found and stack:
            curr, index = stack.pop()
            if index == len(word):
                found = curr[self.EOW]
                continue

            c = word[index]
            if c == ".":
                for child in curr:
                    if child == self.EOW:
                        continue
                    stack.append((curr[child], index + 1))
            elif c in curr:
                nxt = curr[c]
                stack.append((nxt, index + 1))
        return found


# wordDictionary = WordDictionary2()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))
# print(wordDictionary.search("bad"))
# print(wordDictionary.search(".ad"))
# print(wordDictionary.search("b.."))
#
wordDictionary = WordDictionary2()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print(wordDictionary.search("."))
print(wordDictionary.search("a"))
print(wordDictionary.search("aa"))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))
