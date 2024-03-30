from typing import List, Optional


# Definition for a QuadTree node.
class Node:
    EMPTY = -1

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        n = len(grid)

        # 어떤 경우에 차라리 dfs로 grid값이 같은지 확인하는게 좋을까?
        # 같은 값일 경우가 많은 경우에
        # 다른 경우가 많으면  결국 divide conquer + dfs까지해야해서 더 오래 걸림.
        def _construct(ur: int, dr: int, lc: int, rc: int) -> Optional[Node]:
            if ur >= dr and lc >= rc:
                return Node(grid[ur][lc], True, None, None, None, None)
            midR = (ur + dr) // 2
            midC = (lc + rc) // 2
            topLeft = _construct(0, midR, 0, midC)
            topRight = _construct(0, midR, midC + 1, rc)
            bottomLeft = _construct(midR + 1, dr, 0, midC)
            bottomRight = _construct(midR + 1, dr, midC + 1, rc)

            total = topLeft.val \
                    + topRight.val \
                    + bottomLeft.val \
                    + bottomRight.val

            # 현재 노드가 leaf 노드. 자식들은 다 폐기한다.
            if total == 0 or total == (dr - ur + 1) * 2:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(Node.EMPTY, False, topLeft, topRight, bottomLeft, bottomRight)

        return _construct(0, n - 1, 0, n - 1)
