# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getTreeString(self, root):
        if not root:
            return "N"
        return f"*{root.val}_{self.getTreeString(root.left)}_{self.getTreeString(root.right)}*"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.getTreeString(subRoot) in self.getTreeString(root)
        