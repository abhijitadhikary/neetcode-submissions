# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = []
        it = head
        
        while it:
            temp.append(it)
            it = it.next
        
        for idx in range(len(temp)-1, 0, -1):
            temp[idx].next = temp[idx - 1]
        temp[0].next = None
        head = temp[-1]
        return head


                