# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        it = head
        it2 = head.next

        while it2.next:
            if it == it2:
                return True
            it = it.next
            it2 = it2.next
            if it2.next:
                it2 = it2.next
        return False