class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        pos = len(self.data)
        while pos // 2 > 0 and self.data[pos // 2] > item:
            self.data[pos // 2], self.data[pos] = self.data[pos], self.data[pos // 2]
            pos = pos // 2
        print('삽입완료')

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = i * 2
        right = i * 2 + 1
        smallest = i
        if left <= len(self.data)-1 and self.data[left] > self.data[smallest]:
            smallest = left
        print("length {} smallest : {} , left {}, right{}".format(len(self.data), smallest, left, right))
        if right <= len(self.data)-1 and self.data[right] > self.data[smallest]:
            smallest = right
        print("smallest : {} , i {}, length{}".format(smallest, i, len(self.data)))
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]


def heapsort(unsorted):
    H = MaxHeap()

    for item in unsorted:
        H.insert(item)

    sorted = []

    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted


H = MaxHeap()

H.insert(1)
H.insert(2)
H.insert(3)
print(H)

H.remove()


