# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root, best):
        if not root:
            return 0, best
        
        left, bestl = self.height(root.left, best)
        right, bestr = self.height(root.right, best)

        best = max(bestl, bestr, left+right)

        return max(left, right) + 1, best

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height(root, 0)[1]