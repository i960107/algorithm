from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, key: int, item: Any = None):
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def size(self) -> int:
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self) -> int:
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    def lookup(self, key: int, parent=None) -> tuple[Node | None, Node | None]:
        # 재귀적으로 사용하기 위해서 매개변수에 parent필요. root는 parent 없으므로 default값 정해주기

        # 왼쪽 서브 트리를 탐색해야할때
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        # 오른쪽 서브 트리를 탐색해야할때
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        # 지금 노드가 검색하는 값일때
        else:
            return self, parent

    def insert(self, key: int, item: Any = None):
        if key < self.key:
            if self.left:
                return self.left.insert(key, item)
            else:
                self.left = Node(key, item)
        elif key > self.key:
            if self.right:
                return self.right.insert(key, item)
            else:
                self.right = Node(key, item)
        else:
            # 중복 값 넣을 수 없음
            # % .format과 같음.
            raise KeyError('key %s already exists' % key)

    def count_children(self) -> int:
        cnt = 0
        # 자손의 숫자 X 자식의 숫자!!
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def preorder_traverse(self) -> list:
        l = []
        l.append(self.key)
        if self.left:
            l += self.left.preorder_traverse()
        if self.right:
            l += self.right.preorder_traverse()
        return l

    def inorder_traverse(self) -> list:
        l = []
        if self.left:
            l += self.left.inorder_traverse()
        # list합치기
        # append() : 반환된 리스트 자체를 리스트에 원소로 추가하기 때문에 중첩된 리스트 생성됨
        # += :  반환된 리스트를 concat하기 때문에 여기서는 +=를 써줘야함.
        l.append(self.key)
        if self.right:
            l += self.right.inorder_traverse()
        return l

    def postorder_traverse(self) -> list:
        l = []
        # self.left 체크하지않으면 NoneType Attribute Error발생
        if self.left:
            l += self.left.postorder_traverse()
        if self.right:
            l += self.right.postorder_traverse()
        l.append(self.key)
        return l


class BinarySearchTree:
    def __init__(self, root: Node = None):
        # root 없이 빈 트리 생성할 수 있도록 root 기본값 정해주기
        self.root = root

    def size(self) -> int:
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self) -> int:
        # 최대 level +1
        # 재귀 호출하는 함수 안에서는 전체 트리가 빈트리인지 알 수 없다
        # Node클래스에 정의되어 있지 않으면 재귀적으로 서브트리에 대해서 depth 호출할 수 없음
        # 반복문 돌면서 leaf까지 탐색하기.
        if self.root:
            return self.root.depth()
        else:
            return 0

    def insert(self, key: int, item: Any = None):
        # 이진 검색 트리는 삽입되는 위치 key에 따라 정해짐
        if self.root:
            self.root.insert(key, item)
        else:
            self.root = Node(key, item)

    def remove(self, key: int) -> bool:
        # False가 반환되는 경우: 빈트리일때 혹은 빈트리는 아니지만 찾는 키가 없을때
        # self.lookup에서 빈트리 처리하기 때문에 여기서 처리하면 중복된 코드
        # remove는 재귀함수 아님. remove()다시 부르는 일없음. BST클래스에만 존재
        node, parent = self.lookup(key)
        if not node:
            return False
        nChildren = node.count_children()
        # 자식이 없을때
        if nChildren == 0 or nChildren == 1:
            # nChildren ==0인 경우와 함께 처리 가능
            # node의 자식이 0개인경우 parent 포인터에 None 대입됨
            child = node.left if node.left else node.right
            if parent and parent.key > node.key:
                parent.left = child
            elif parent and parent.key < node.key:
                parent.right = child
            else:
                self.root = child
        # 자식이 2명. 이진 트리. 삭제되는 node를 오른쪽 서브트리의 가장 작은 값이 대체.
        # 오른쪽 서브트리의 가장 작은 값으로 대체하면 전체적으로 트리의 구조는 유지됨.
        # 왼쪽 서브트리의 가장 큰 값도 가능
        # 트리를 삭제할때는 항상 삭제하려는 노드의 parent도 알고 있어야 자식들을 parent와 연결해줄 수 있음
        else:
            predecessor = node
            successor = node.right

            # 오른쪽 서브트리에서 가장 작은 원소가 삭제되는 노드를 대신함
            # 오른쪽 서브트리에서 가장 작은 원소가 삭제되는 노드의 왼쪽 서브트리의 값보다 큰 원소중 가장 작은 원소임.
            # successor의 left tree가 None일때까지 leaf node가 될때까지는 아님. right subtree있을수있음
            while successor.left:
                predecessor = successor
                successor = successor.left

            # Node자체를 대체하는게 아니라 key와 item만 가지고 오고
            # link는 유지
            node.key = successor.key
            node.item = successor.item

        if parent.key < successor.key:
            parent.right = successor.right
        else:
            parent.left = successor.right
        return True

    def lookup(self, key: int) -> tuple[Node | None, Node | None]:
        # 찾은 노드와, 부모노드를 반환 -> remove()에 사용됨
        # 값 여러개 반환시 tuple로 반환됨. type 힌트 주의
        # Node.lookup()과 BinarySearchTree.lookup() 매개변수 다름.

        if self.root:
            return None, None
        else:
            return self.root.lookup(key, None)

    def preorder_traverse(self) -> list:
        # 트리 자체에 대해서 재귀적으로 호출할 수 없음
        # 특정 노드에 대해 재귀적으로 호출해야함. 트리를 재귀적으로 정의한다는건 특정 노드부터 시작하는 것.
        if not self.root:
            return []
        else:
            return self.root.preorder_traverse()

    def inorder_traverse(self) -> list:
        # 이진 검색트리의 중위 순회 결과는 오름차순 정렬되어있음
        # 트리 자체에 대해서 재귀적으로 호출할 수 없음
        # 특정 노드에 대해 재귀적으로 호출해야함. 트리를 재귀적으로 정의한다는건 특정 노드부터 시작하는 것.
        if not self.root:
            return []
        else:
            return self.root.inorder_traverse()

    def postorder_traverse(self) -> list:
        if not self.root:
            return []
        else:
            return self.root.postorder_traverse()

    def max(self) -> int | None:
        # 재귀적으로도 구현 가능
        # 이렇게 정의하면 문제점은?
        # 가장 작은 key 값 혹은 빈트리일지 None 반환. type hint : from__future__ import annotations로 |로 가능.
        if self.root:
            curr = self.root
            while curr.right:
                curr = curr.right
            return curr.key
        else:
            return None

    def min(self) -> int | None:
        if self.root:
            curr = self.root
            while curr.left:
                curr = curr.left
            return curr.key
        else:
            return None


# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(2)
# bst.insert(9)
# bst.insert(1)
# bst.insert(4)
# bst.insert(6)
# bst.insert(12)
# bst.insert(8)
# bst.insert(10)
# bst.insert(13)
# bst.insert(7)
# print(bst.inorder_traverse())
# print(bst.max())
# print(bst.min())
# bst.remove(9)
# print(bst.inorder_traverse())
# 내림차순 정렬 어떻게? - inorder/postorder/preorder다 아님. 오른쪽 서브트리->자신-> 왼쪽서브트리 순으로 순회

# ------------------------------------------
'''doit 자료구조와 함께 배우는 알고리즘 입문 이진 검색 트리 구현'''


class DoNode:
    def __init__(self, key: Any, value: Any, left: DoNode = None, right: DoNode = None):
        # 노드의 키 값을 Any로 하는 이유. 문자열을 key로 할 수  있음
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class DoBinarySearchTree:
    def __init__(self):
        # 빈 이진트리로 생성
        self.root = None

    def search(self, key: Any) -> Any:
        '''키 값으로 노드를 검색 후 노드의 value를 반환'''
        curr = self.root
        # 키를 찾거나, 더 이상 검색할 키가 없는 경우 반복 종료.
        # 위 코드와 달리 재귀적으로 정의하지 않음. iterative version.
        # search함수가 value가 아니라 Node자체를 반환하면 remove시에도 쓸 수 있으니 좋다.
        while curr and curr.key != key:
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        # 빈트리거나 찾는 값이 없을때 curr is None
        return curr.value if curr else None

    def add(self, key: Any, value: Any) -> bool:
        '''키가 key이고 값이 value인 노드를 삽입'''

        # 재귀적 함수 정의하지만, Node 클래스에 정의하는게 아니라 inner function 사용
        # inner function 사용시 1)글로벌 함수로 정의하는게 아니라 그 함수만 접근 가능  encasulation
        # 2) enclosing function의 지역번수 사용가능
        def add_node(node: DoNode, key: Any, value: Any) -> bool:
            '''node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입'''
            if key == node.key:
                return False
            if key < node.key:
                if node.left:
                    add_node(node.left, key, value)
                else:
                    node.left = DoNode(key, value)
            else:
                if node.right:
                    add_node(node.right, key, value)
                else:
                    node.right = DoNode(key, value)
            # False 반환 되지 않고, 여기까지 왔다는건 재귀 호출 끝나고 삽입 된 후라는 뜻
            return True

        if self.root:
            return add_node(self.root, key, value)
        else:
            # 빈트리인지 아닌지는 여기서만 알 수 있음
            self.root = DoNode(key, value)
            return True

    def remove(self, key: Any) -> bool:
        '''키가 key인 노드를 삭제'''
        curr = self.root
        parent = None
        # 매번 키값을 확인하거나 flag생성해두기
        is_left_child = False

        #왜 재귀적 아니고 iterative version했을까
        while True:
            # 삭제할 키를 검색. 빈트리이거나 삭제할 키를 찾지 못하면 return False
            if not curr:
                return False
            if curr.key > key:
                parent = curr
                curr = curr.left
                is_left_child = True
            elif curr.key < key:
                parent = curr
                curr = curr.right
                is_left_child = False
            else:
                break

        # 오른쪽 자식만 있거나 자식이 없는경우
        if not curr.left:
            # root 인경우
            if parent and is_left_child:
                parent.left = curr.right
            elif parent and not is_left_child:
                parent.right = curr.right
            else:
                self.root = curr.right
        # 왼쪽 자식만 있거나 자식이 없는경우
        # 삭제하려는 노드의 자식이 없는 경우에 부모 포인터가 None을 가리키게 됨
        elif not curr.right:
            if parent and is_left_child:
                parent.left = curr.left
            elif parent and not is_left_child:
                parent.right = curr.left
            else:
                self.root = curr.left
        # 자식이 2명인경우
        else:
            # 왼쪽 서브트리에서 키값이 가장 큰 노드를 검색한 후 삭제하려는 위치로 복사하고, 기존 노드를 삭제
            # 삭제하려는 위치 curr 만 기억하고 있으면 됨. parent, is_left_child 덮어써도됨
            parent = curr
            successor = curr.left
            is_left_child = True
            while successor.left:
                parent = successor
                successor = successor.right
                is_left_child = False
            curr.key = successor.key
            curr.value = successor.value
            # successor는 왼쪽 서브트리만 존재할 것
            if is_left_child:
                parent.left = successor.left
            else:
                parent.right = successor.left

        return True

    def dump(self, reverse=False) -> None:
        '''모든 노드를 키의 오름차순/내림차순으로 출력(inorder_traverse)'''

        # 재귀적으로 정의하려면 별도의 함수가 무조건 필요한가?
        # dump()함수는 트리에 대해 오름차순 출력하기 위한 함수로 매개변수 없지만
        # get_subtree()의 경우에는 재귀적으로 밑에 트리부터 올라와야하기 때문에 node를 매개변수로 받아야함
        # 따라서 별도의 함수 필요
        # inner function에서는 self 매개변수로 넘기지 않음
        def print_subtree(node: DoNode) -> None:
            '''node를 루트로 하는 서브트리(자신 포함)의 노드를 키의 오름차순 출력 (key value) 형식'''
            # 빈 트리 처리
            if node:
                # 동기적으로 일어나므로 오름차순 출력됨. 왼쪽 서브트리 모두 출력되고 난 후->자신->오른쪽 서브트리 출력됨
                # node.left 확인하지 않아도 됨. 호출된 함수 안에서 체크하기 때문
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_reverse(node: DoNode) -> None:
            # 왜 9가 빠지지?
            '''node를 루트로 하는 서브트리(자신 포함)의 노드를 키의 내림차순 출력 (key value) 형식'''
            if node:
                print_subtree_reverse(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_reverse(node.left)
            # else:
            # 빈트리일때 [] 출력하면 leaf 노드 마다 []가 출력됨.
            # []출력하고 싶다면 전체가 빈트리일때만 즉, dump()쪽에서 처리해줘야함.
            #     print([])

        if self.root:
            if not reverse:
                print_subtree(self.root)
            else:
                print_subtree_reverse(self.root)
        else:
            print([])

    def min_key(self) -> Any:
        '''최소 키를 반환'''
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.key if curr else None

    def max_key(self):
        '''최대 키를 반환'''
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.key if curr else None


dbst = DoBinarySearchTree()
dbst.add(1, '수연')
dbst.add(10, '예지')
dbst.add(5, '동혁')
dbst.add(12, '원준')
dbst.add(14, '민서')
print(f'이 키를 갖는 값은 {dbst.search(5)} 입니다')
dbst.dump()
dbst.remove(10)
dbst.dump(reverse=True)
print(f'키의 최솟값은 {dbst.min_key()}')
print(f'키의 최댓값은 {dbst.max_key()}')
