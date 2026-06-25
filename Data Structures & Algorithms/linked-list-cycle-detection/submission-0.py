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
        seen = set()

        while it:
            if it in seen:
                return True
            else:
                seen.add(it)
                it = it.next
        return False