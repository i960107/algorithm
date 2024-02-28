from typing import List
from collections import defaultdict, deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = 8
        gene = ['A', 'C', 'G', 'T']

        # wordLadder와 같은 문제일까?
        # 변할 수 있는 characterrk 4개로 한정되어 있으므로 글자 하나씩 바꿔서 비교해도 충분히 가능.
        # Mutation < wordLadder 난이도 더 어려움.
        if endGene not in bank:
            return -1

        bank.append(startGene)

        graph = defaultdict(list)
        for gene in bank:
            for i in range(n):
                pattern = gene[:i] + '*' + gene[i + 1:]
                graph[pattern].append(gene)

        dist = 0
        queue = deque([startGene])
        visited = {startGene}

        while queue:
            dist += 1
            for _ in range(len(queue)):
                gene = queue.popleft()
                for i in range(n):
                    pattern = gene[:i] + '*' + gene[i + 1:]
                    for nxt in graph[pattern]:
                        if nxt in visited:
                            continue
                        visited.add(nxt)
                        if nxt == endGene:
                            return dist
                        queue.append(nxt)

        return -1

    def minMutation2(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = 8
        chars = ['A', 'C', 'G', 'T']
        bank = set(bank)
        if endGene not in bank:
            return -1
        bank.add(startGene)

        def getMutations(gene: str) -> List[str]:
            mutations = []
            for i in range(len(gene)):
                for c in chars:
                    if gene[i] == c:
                        continue
                    mutations.append(gene[:i] + c + gene[i + 1:])
            return mutations

        def isValidMutation(mutation: str) -> bool:
            return mutation in bank

        graph = defaultdict(set)
        for gene in bank:
            for mutation in getMutations(gene):
                if not isValidMutation(mutation):
                    continue
                graph[gene].add(mutation)
                graph[mutation].add(gene)

        dist = 0
        queue = deque([startGene])
        visited = {startGene}

        while queue:
            dist += 1
            for _ in range(len(queue)):
                gene = queue.popleft()
                for i in range(n):
                    for nxt in graph[gene]:
                        if nxt in visited:
                            continue
                        visited.add(nxt)
                        if nxt == endGene:
                            return dist
                        queue.append(nxt)

        return -1


s = Solution()
print(s.minMutation2(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
