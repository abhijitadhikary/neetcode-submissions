# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        it2 = head

        while fast and fast.next and it2.next and it2.next.next:
            slow = slow.next
            fast = fast.next.next
            it2 = it2.next.next.next

            if fast == slow or slow == it2 or fast == it2:
                return True
        return False