from typing import List


class Node:
    def __init__(self):
        # { 문자: 자식 노드들}
        self.children = dict()
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[curr]
        curr.isEndOfWord = True

    def insert_recursive(self, word: str):
        def _insert_recursive(node: Node, word: str):
            if len(word) == 0:
                node.isEndOfWord = True
                return

            c = word[0]

            if c not in node.children:
                node.children[c] = Node()
            _insert_recursive(node.children[c], word[1:])

        return _insert_recursive(self.root, word)

    def search_recursive(self, word: str):

        # 못핮으면 None 반환, 글자의 마지막 노드 반환
        def __search__(node: Node, word: str):
            if not word:
                return node if node.isEndOfWord else None
            c = word[0]
            if c not in node.children:
                return None
            return __search__(node.children[c], word[1:])

        return __search__(self.root, word)

    def autocomplete(self, prefix: str) -> List[str]:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        return self.search_start_with(curr, prefix)

    def search_start_with(self, node: Node, prefix: str) -> List[str]:
        result = []
        if node.isEndOfWord:
            result.append(prefix)

        for c, child in node.children.items():
            result += self.search_start_with(child, prefix + c)

        return result
