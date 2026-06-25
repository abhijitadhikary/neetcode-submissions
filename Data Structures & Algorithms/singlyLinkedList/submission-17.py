class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.back = None
    
    def get(self, index: int) -> int:
        if ((index < 0) or (self.head is None)):
            return -1
        else:
            traverseNode = self.head
            traverseIndex = 0
            while(traverseNode and (traverseIndex < index)):
                traverseNode = traverseNode.next
                traverseIndex += 1
            
            if (not traverseNode is None):
                return traverseNode.val
            else:
                return -1

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, index: int) -> bool:
        if ((index < 0) or (self.head is None)):
            return False
        else:
            if (index == 0):
                if (self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                traverseIndex = 1
                back = self.head
                front = self.head.next

                while ((not front is None) and (traverseIndex < index)):
                    front = front.next
                    back = back.next
                    traverseIndex += 1

                if (not front is None):
                    back.next = front.next
                    if front == self.tail:
                        self.tail = back
                else:
                    return False
            return True

    def getValues(self) -> List[int]:
        nodeList = []
        traverseNode = self.head
        while (not traverseNode is None):
            nodeList.append(traverseNode.val)
            traverseNode = traverseNode.next
        return nodeList