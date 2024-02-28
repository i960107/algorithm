from typing import List, Dict
from collections import defaultdict, deque
from copy import deepcopy
import heapq


class SolutionFail:
    # TIME LIMIT EXCEED
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        # 거리가 1인 단어를 빠르게 찾는 방법 없을끼?
        def isAdjacent(word1: str, word2: str) -> bool:
            count = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    continue
                count += 1
                if count >= 2:
                    break
            return count == 1

        graph = defaultdict(list)
        for i in range(len(wordList)):
            word1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                word2 = wordList[j]
                if isAdjacent(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        # bfs는 넓이 우선 탐색만. 최단거리는 heap필요. 아님!!!!!!!!!!

        # bfs의 중복 방지 어떻게..?
        # set 말고 다른 방법이 없나.
        queue = deque([(0, beginWord)])
        visited = set()

        # 가장 가까운 것부터 빼낼때 heap안 써도 가장 가까운 것부터 빼내지나? 맞음.
        # word가 이미 방문체크되었을수도 있음.!!!!!
        # 방문체크를 언제하는게 좋을까?
        while queue:
            dist, word = queue.popleft()

            if word in visited:
                continue

            visited.add(word)
            dist += 1

            if word == endWord:
                return dist

            for nxt in graph[word]:
                # visited가 공유되는 변수인데 여기서 이러면 안됨...?
                # 최단 경로로 방문할 거기 때문에 한번 방문했다면 다음에는 고려안해도됨.
                # new_visited = deepcopy(visited)
                # new_visited.add(nxt)
                queue.append((dist, nxt))
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # isAdjacent랑 time complexity 비교?
        # 길이가 1인 단어 비교 -> O(N^2*M) vs O(N*M)
        def makePattern(word: str) -> List[str]:
            patterns = []
            for i in range(len(word)):
                patterns.append(word[:i] + '*' + word[i + 1:])
            return patterns

        def makePatternGraph(words: List[str]) -> Dict:
            graph = defaultdict(list)
            for word in words:
                for pattern in makePattern(word):
                    graph[pattern].append(word)
            return graph

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        patternGraph = makePatternGraph(wordList)

        # visited를 공유해도 되나..?
        visited = {beginWord}
        q = deque([beginWord])
        result = 1

        while q:
            # 거리를 매번 기억하지 않기 위해 같은 거리에 있는 노드들을 한꺼번에 꺼낸다.
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for pattern in makePattern(word):
                    for nxt in patternGraph[pattern]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
            result += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        wordList.append(beginWord)

        def makePatternFromWord(word: str) -> List[str]:
            pattern = []
            for i in range(len(word)):
                pattern.append(word[:i] + '*' + word[i + 1:])
            return pattern

        # make Graph
        graph = defaultdict(list)
        for word in wordList:
            for p in makePatternFromWord(word):
                graph[p].append(word)

        queue = deque([beginWord])
        dist = 0
        visited = {beginWord}

        while queue:
            dist += 1
            count = len(queue)

            for _ in range(count):

                word = queue.popleft()

                for p in makePatternFromWord(word):
                    for nxt in graph[p]:
                        if nxt in visited:
                            continue
                        if nxt == endWord:
                            return dist + 1
                        visited.add(nxt)
                        queue.append(nxt)
        return 0


s = Solution()
print(s.ladderLength2(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength2(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", ]))
print(s.ladderLength2("cet", "ism",
                      ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val",
                       "mes", "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue",
                       "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan",
                       "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump", "dis", "ads",
                       "max", "jaw", "out", "btu", "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
                       "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie",
                       "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac", "nut", "why",
                       "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
                       "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara",
                       "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
                       "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron",
                       "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen",
                       "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod", "hun", "gyp",
                       "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere", "dig", "era", "cat", "fox",
                       "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
                       "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
                       "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six",
                       "ila", "lao", "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may",
                       "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den",
                       "fla", "auk", "cox", "ibo", "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
                       "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep", "owe", "ind", "hog", "eve",
                       "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao",
                       "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem", "who", "bet",
                       "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
                       "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
                       "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy",
                       "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm",
                       "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd",
                       "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue", "dim",
                       "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
                       "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton", "sol", "din",
                       "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
                       "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two",
                       "ins", "con", "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow",
                       "sal", "sic", "ted", "wot", "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
                       "err", "him", "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego", "mac", "baa", "min", "com",
                       "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top",
                       "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac", "fed", "goo", "tee", "ell",
                       "not", "act", "gil", "rut", "ala", "ape", "rig", "cid", "god", "duo", "lin", "aid", "gel", "awl",
                       "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
                       "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob",
                       "mow", "jot", "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got",
                       "meg", "zoe", "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"]))
