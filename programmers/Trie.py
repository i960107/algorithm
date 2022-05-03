from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word = False
        # dict 형
        # children : key는 문자열 value는 TrieNode?
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        '''트라이에 word 삽입'''
        node = self.root
        for char in word:
            node = node.children[char]
        # word의 마지막 node에 대해서 True. 단어가 완성되었을때
        node.word = True

    def search(self, word: str) -> bool:
        '''word와 일치하는 단어가 있다면 True반환'''
        node = self.root
        for char in word:
            # root는 None. key값을 가지지 않음
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        '''word로 시작하는 단어가 있다면 True반환'''
        node = self.root
        for char in prefix:
            # root는 None. key값을 가지지 않음
            if char not in node.children:
                return False
            node = node.children[char]
        return True


t = Trie()
t.insert("apple")
t.insert("apeal")
t.insert("apear")
print(t.search("apple"))
print(t.search("appealr"))
print(t.search("abc"))
