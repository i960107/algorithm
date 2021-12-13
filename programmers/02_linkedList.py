class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = node(None)
        self.tail = None
        self.head.next = self.tail
    
    def getNodeCount(self):
        return self.nodeCount

    def getAt(self, pos):
        if pos < 0 or pos >self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i+=1

        return curr

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.apeend(curr.data)
        return result

    def insertAfter(self, prev, newNode):
        if prev == None or newNode == None:
            return False

        newNode.next = prev.next
        prev.next= newNode

        if prev.next is None:
            self.tail = newNode

        self.nodeCount +=1

        return True

