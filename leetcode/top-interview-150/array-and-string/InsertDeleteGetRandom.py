# 빈 상태에서 getRandom 호출하지 않음
# 같은 확률로 return되어야함.
import random
from collections import deque


# same probability -> set구성 자체가 달라지면?
# set [2,3] 2가 한번 불린상태에서 4가 삽입되고 [2,3,4]에서 같은 확률로 리턴된다는 것은 무슨 의미인가?
# 2는 이미 한번 불렸으니깐 3,4가 50%의 확률로 리턴된다?
# 확률이 같아야한다 아님.
class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.called = set()


    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.remove(val)
        if val in self.called:
            self.called.remove(val)
        return True

    # set은 index로 pop할 수 없는데 어쩌지...
    # 한번씩 pop되면 다시 모든 원소들이 후보가 될 수 있음.
    # each function works in O(1) time complexity. TLE
    def getRandomFail(self) -> int:
        l = list(self.set)
        while True:
            random_num = random.choice(l)
            if random_num in self.called:
                continue
            self.called.add(random_num)
            if len(self.called) == len(self.set):
                self.called.clear()
            return random_num

    def getRandom(self) -> int:
        l = list(self.set)
        while True:
            random_num = random.choice(l)
            if random_num in self.called:
                continue
            self.called.add(random_num)
            if len(self.called) == len(self.set):
                self.called.clear()
            return random_num


class RandomizedSet2:

    def __init__(self):
        self.data_map = {}  # key=element, val=index in data array
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data.append(val)
        self.data_map[val] = len(self.data) - 1
        return True

    # Steps:
    # 1.) Swap last value with removal value in the array
    # 2.) Update hashmap with the updated index of the last index
    # 3.) Remove last element from array and remove val from hashmap
    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False

        last_data = self.data.pop()

        if last_data != val:
            removal_idx = self.data_map[val]
            self.data[removal_idx] = last_data
            self.data_map[last_data] = removal_idx

        del self.data_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


r = RandomizedSet()
r.insert(1)
r.insert(2)
r.insert(3)
r.insert(4)
print(r.getRandom())
print(r.getRandom())
print(r.getRandom())
print(r.getRandom())
print(r.getRandom())
