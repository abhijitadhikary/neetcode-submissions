class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if index < 0 or self.head is None:
            return -1
        
        traverseNode = self.head
        traverseIndex = 0

        while(not traverseNode is None and traverseIndex < index):
            traverseIndex += 1
            traverseNode = traverseNode.next
        
        if not traverseNode is None:
            return traverseNode.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            front = self.head
            back = None
            traverseIndex = 0

            while(not front is None and traverseIndex < index):
                if traverseIndex == 0:
                    back = self.head
                else:
                    back = back.next
                front = front.next
                traverseIndex += 1
            
            if not front is None:
                back.next = front.next
                if front == self.tail:
                    self.tail = back
            else:
                return False

        return True



    def getValues(self) -> List[int]:
        nodeList = []
        traverseNode = self.head

        while(not traverseNode is None):
            nodeList.append(traverseNode.val)
            traverseNode = traverseNode.next

        return nodeList
