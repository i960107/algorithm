from typing import List, Optional
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialization(self, root: TreeNode) -> str:
        '''트리 bfs직렬화'''
        # 이진트리의 데이터 구조는 논리적인 구조.
        # 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔워쟈함
        # 직렬화
        # pickle모듈 -> hierarchy구조를 byte stream으로 변경하는 작업. flattening

        # 정답이 string이고 값이 누적되는 것이라면 string은 immutable객체로 변경시 새로 생성해
        # 메모리 효율 좋지 않음. 배열로 만든 후 후에 string변환이 좋은 방법
        # 인덱스 계산 쉽게 하기 위해 0번째 인덱스 비워두기
        answer = ['#']
        q = deque([root])
        while q:
            # 값이 없으면 None 삽입
            curr = q.popleft()
            if curr:
                answer += [str(curr.val)]
                # leaf노드의 왼쪽 오른쪽 자식도 삽입됨.
                q.append(curr.left)
                q.append(curr.right)
            else:
                answer += ["#"]

        return ''.join(answer)

    def deserialization(self, data: str) -> Optional[str]:
        # 빈 트리일 경우 예외 처리
        if data == "##":
            return None

        # 그냥 string도 index로 참조할 수 있지 않나?
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
