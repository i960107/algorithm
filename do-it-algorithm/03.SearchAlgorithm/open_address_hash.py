from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib


# Enum 클래스를 선언하는 법
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = -2


class Bucket:
    '''해시를 구성하는 노드'''

    # 파이썬은 변수의 타입이 동적으로 결정됨. 어떤 값이 할당되느냐에 따라서 변수의 타입이 자동으로 결정
    # 런타임 AttributeError발생가능
    # 정적으로 타입 선언해서 실수 방지 가능
    def __init__(self, key: Any = None, value: Any = None, status: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set(self, key: Any, value: Any, status: Status) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status):
        self.status = status


class OpenAddressHash:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [Bucket()] * capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        '''재해시값을 구함'''
        # key값 자체에 1을 더하는게 아니라 구한 해시값에 1을 더해서 재해시
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        '''키가 key인 버킷을 검색'''
        hash = self.hash_value(key)
        curr = self.table[hash]

        # 전체 해시 테이블이 다 차있을때 순환문 종료 while 보다 for문이 적합. 해시 테이블의 capacity만큼만 반복
        for i in range(self.capacity):
            if curr.status == Status.EMPTY:
                break
            elif curr.status == Status.OCCUPIED and curr.key == key:
                return curr
            else:  # curr.status == Status.DELETED or curr.key !=key
                hash = self.rehash_value(hash)
                curr = self.table[hash]
        return None

    def search(self, key: Any) -> int:
        '''키가 key인 원소를 검색하여 반환'''
        node = self.search_node(key)
        return node.value if node else None

    def remove(self, key: Any) -> bool:
        curr = self.search_node(key)
        if curr:
            curr.key = None
            curr.value = None
            curr.set_status(Status.DELETED)
            return True
        else:
            return False

    def add(self, key: Any, value: Any) -> bool:
        # search_node를 사용하면 안됨? 됨. search_node/search모두 키가 = key인 버킷이 없으면 None을 반환
        if self.search_node(key):
            return False
        hash = self.hash_value(key)
        curr = self.table[hash]

        for i in range(self.capacity):
            if curr.status == Status.OCCUPIED:
                hash = self.rehash_value(hash)
                curr = self.table[hash]
            else:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
        return False

    def dump(self) -> None:
        '''테이블의 모든 원소를 출력(덤프 트럭에서 짐이 한번에 내리는 모습)'''
        for i in range(len(self.table)):
            curr = self.table[i]
            print(f'{i : 2}', end='')
            if curr.status == Status.OCCUPIED:
                print(f'  -> {curr.key}({curr.value})')
            elif curr.status == Status.DELETED:
                print('--삭제 완료--')
            elif curr.status == Status.EMPTY:
                print('--미등록--')


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


hash = OpenAddressHash(13)

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
