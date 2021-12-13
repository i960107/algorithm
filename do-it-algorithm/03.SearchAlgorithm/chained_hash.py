# interpreter를 update하지 않고 최신 버전의 기능 사용
from __future__ import annotations
from typing import Any, Type
import hashlib
from enum import Enum


class Node:
    '''해시를 구성하는 노드'''

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        # 만약 값이 없고 키만 있는 데이터의 해시 테이블을 사용하고 싶다면
        # value 에 key값을 전달
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    '''체인법으로 해시 클래스 구현'''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_value(self, key: Any) -> int:
        '''해시 값 구하기'''
        if isinstance(key, int):
            return key % self.capacity
        # key 가 정수형이 아닌 경우 표준라이브러리로 형 변환 해 해시값 얻기
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any):
        '''키가 key인 원소를 검색하여 값을 반환'''
        hash_value = self.hash_value(key)
        curr = self.table[hash_value]
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        raise ValueError

    def add(self, key: Any, value: Any) -> bool:
        '''키가 key이고 값이 value인 원소를 추가'''
        hash_value = self.hash_value(key)

        curr = self.table[hash_value]
        # 같은 키값이 있으면 실패
        while curr:
            if curr.key == key:
                return False
            curr = curr.next
        # 해시값의 버킷의 맨 앞에 노드를 추가
        # 맨 뒤에 추가하는 것과 복잡도 어떻게 차이가 있지?
        self.table[hash_value] = Node(key, value, self.table[hash_value])
        return True

    def remove(self, key: Any) -> bool:
        '''키가 key인 원소 삭제'''
        hash_value = self.hash_value(key)

        curr = self.table[hash_value]
        # 그 전 노드를 기억하고 있거나 vs 그 후 노드를 검사하거나
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[hash_value] = curr.next
                return True
            else:
                prev = curr
                curr = curr.next
        return False

        # if not curr:
        #     return False
        # elif curr.key == key:
        #     self.table[hash_value] = curr.next
        #     return True
        # else:
        #     while curr.next:
        #         if curr.next.key == key:
        #             curr.next = curr.next.next
        #             return True
        #     return False

    def dump(self) -> None:
        '''테이블의 모든 원소를 출력(덤프 트럭에서 짐이 한번에 내리는 모습)'''
        for i in range(len(self.table)):
            curr = self.table[i]
            print(i, end='')
            while curr:
                # 원소가 존재하면 앞에 -> 넣기
                print(f'  -> {curr.key}({curr.value})', end='')
                curr = curr.next
            print()


Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    '''메뉴 선택'''
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='    ', end='')
        try:
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)
        except ValueError:
            pass


hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력하세요 : '))
        value = input('추가할 값을 입력하세요 : ')
        if not hash.add(key, value):
            print('추가를 실패했습니다!')
    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요 : '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')
    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요 : '))
        try:
            value = hash.search(key)
            print(f'검색한 키를 갖는 값은 {value}입니다')
        except ValueError:
            print('검색값을 갖는 데이터가 없습니다')
    elif menu == Menu.덤프:
        hash.dump()
    else:
        break
