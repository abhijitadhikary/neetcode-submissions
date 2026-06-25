# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def parseTree(self, t1, t2):
        
        if not t1 and not t2:
            return True
        if (not t1 or not t2) and (t1 != t2):
            return False
        
        if t1.val != t2.val:
            return False

        left = self.parseTree(t1.left, t2.left)
        right = self.parseTree(t1.right, t2.right)

        return left and right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.parseTree(p, q)