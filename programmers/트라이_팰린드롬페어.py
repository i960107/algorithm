from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        # dict 형
        # children : key는 문자열 value는 TrieNode?
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @staticmethod  # 데코레이터
    # JAVA static 메소드 선언. 파라미터에 self가 빠져있음
    # 클래스에 속하는 메소드가 아닌 독립적인 function의 의미. 클래스 바깥에 선언한 것과 같은 의미
    # 여기서는 왜 static으로 선언했을가? 다른 모듈에서도 사용할 수 있게? Trie 자료구조와 상관 없어서?
    def is_palindrome(word: str) -> bool:
        return word[::] == word[:: -1]

    def insert(self, index: int, word: str):
        '''트라이에 word 삽입'''
        node = self.root
        # 팰린드롬 판별 위해 뒤집어서 트라이로 구성
        for i, char in enumerate(reversed(word)):
            # staticmethod 안 붙여주면 warning 뜸
            # str list slicing한 결과 str
            if Trie.is_palindrome(word[:len(word) - i]):
                # 여기까지 문자가 palindrome인지
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        # word_id  각 단어가 끝나는 지점에서 True,False 대신 index 저장
        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        '''word와 일치하는 단어가 있다면 True반환'''
        # 입력값을 각각 한번씩만 대입하면 되기 때문에 O(N) 풀이
        # 단어의 최대 길이를 k로 했을때 O(K^2n)
        result = []
        node = self.root

        while word:
            # 판별 로직 3: 끝나는 지점의 word_id 값이 -1이 아니라면 words[index] 와 words[word_id]는 팰린드롬 관계
            # 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if Trie.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별로직 1: 끝가지 탐색했을때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별로직 2: 끝까지 탐색했을때 panlindrome_word_ids가 있는 경우
        # 트라이 삽입 중에 남아있는 단어가 팰린드롬이라면 미리 팰린드롬 여부를 세팅해 두기
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result


class Solution:
    def palindrome_pairs(self, words: List[str]) -> List[List[int]]:
        # 모든 입력값을 트라이로 만들어두고 딱 한번씩만 탐색
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


s = Solution()
# 왜 23  안되지? 당연히 안되지 바보야!
print(s.palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
