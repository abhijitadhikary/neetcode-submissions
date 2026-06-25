# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root, dist_most):
        if not root:
            return 0, dist_most
        
        height_l, dist_most_l = self.height(root.left, dist_most)
        height_r, dist_most_r = self.height(root.right, dist_most)

        dist_most = max(dist_most_l, dist_most_r, abs(height_l - height_r))
        return max(height_l, height_r)+1, dist_most


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root, 0)[1] <= 1