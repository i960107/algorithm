# 문자열 검색에 최적화된 자료구조 -> 검색, 자동완성, spellcheck 등에 활용 가능

class Node:
    def __init__(self):
        # 알파벳으로 26자리 배열 해도 됨. -> 메모리 낭비 될 수도.
        self.children = dict()
        self.isEndOfWord = False


# 빈 문자열은 input으로 주어지지 않음
class Trie:
    def __init__(self):
        self.root = Node()

    # 중복된 문자가 입력되어도 됨. 수정되는 데이터 없음
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEndOfWord == True

    # return True. 이전에 입력된 단어들 중 prefix로 가지는 단어가 있다면
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
