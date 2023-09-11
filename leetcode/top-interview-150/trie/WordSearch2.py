from typing import List, Dict
from collections import defaultdict


class Solution:
    # 인접할 셀들을 방문하며 만들수 있는 글자 수.
    # 한 셀은 한번 이상 사용될 수 없다.
    # 한번 이상 발견되면 그만.
    # time limit 줄일 수 있도록 words -> set(words)
    # basic idea : trie로 문자열을 효율적으로 검색하고, dfs로 가능한 모든 경로를 탐색한다는 것이다. 백트래킹할지말지 trie에 있는지 없는
    def findWordsFail(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        di = (0, 0, 1, -1)
        dj = (1, -1, 0, 0)

        # 재귀에서 pop() 하는 위치
        def dfs(i: int, j: int, visited: List[List[bool]], depth: int, target: str):
            if target[depth] != board[i][j]:
                return False

            if depth == len(target) - 1:
                return True

            visited[i][j] = True

            found = False
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if not ((0 <= ni < m) and (0 <= nj < n)):
                    continue
                if visited[ni][nj]:
                    continue
                found = dfs(ni, nj, visited, depth + 1, target)
                if found:
                    break

            visited[i][j] = False
            return found

        d = defaultdict(list)
        # 모든 단어에 대해서 재귀를 수행하는게 아니라, 전체 dfs한 것에서 words가 있는지 찾는다?
        for i in range(m):
            for j in range(n):
                d[board[i][j]].append((i, j))

        visited = [[False] * n for _ in range(m)]
        result = []
        # 중복된 단어가 있는지 확인한다.
        # target만 체크하는게 문제. -> 후보에 없다면 어떻게 체크하지.
        for word in set(words):
            found = False
            for i, j in d[word[0]]:
                if found:
                    continue
                found = dfs(i, j, visited, 0, word)
                if found:
                    result.append(word)

        return result

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        di = (0, 0, 1, -1)
        dj = (1, -1, 0, 0)

        EOW = "EOW"
        root = dict()
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr[EOW] = True

        # trie에서 eow에서 string 찾을 수 있는 방법?
        def dfs(i: int, j: int, visited: List[List[bool]], children: Dict[str, List[str]], path: List[str]):
            visited[i][j] = True
            path.append(board[i][j])

            children = children[board[i][j]]
            if EOW in children:
                result.add(''.join(path))

            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if not ((0 <= ni < m) and (0 <= nj < n)):
                    continue
                if visited[ni][nj]:
                    continue
                if board[ni][nj] not in children:
                    continue
                dfs(ni, nj, visited, children, path)

            visited[i][j] = False
            path.pop()

        visited = [[False] * n for _ in range(m)]
        path = []
        result = set()

        # visited를 사용하지 않아도 되는 이유
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, visited, root, path)
        return list(result)

    def findWordsOptimized(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # Get the letter at the current position on the board
            letter = board[x][y]
            # Traverse the trie to the next node
            cur = root[letter]
            # Check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            # Mark the current position on the board as visited
            board[x][y] = '*'
            # Recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # Restore the original value of the current position on the board
            board[x][y] = letter
            # If the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)

        # Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word

        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Initialize a list to store the results
        res = []


s = Solution()
print(s.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                  words=["oath", "pea", "eat", "rain"]))
print(s.findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
                  ["oa", "oaa"]))
