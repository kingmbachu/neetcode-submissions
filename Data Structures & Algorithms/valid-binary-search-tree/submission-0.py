# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #R: The question is asking us to return true if its a valid BST or false if its not a valid BST. For it to be a valid BST, we need to ensure that the lEFT child is less than the root and the RIGHT child is greater than than the root.
        #E: i) Empty root means it is not a BST. ii) if it only contains a root, then it is not a valid BST, return false.
        #A: My approach to this problem would be to keep track of our root always because our root will always help in determinging wheter its a valid BST. So, essentially, if we are on the LHS. we need to check if the lhs is less than the root, and then check its subtrees and apply the same logic there, but lets say we had a another subtree, we would be comparing the current node val to its current parent and the root we said we would always keep track of. and we would apply the same logic to the RHS. And this would lead to a time complexity of O(n) and space complexity of O(n).
        #C:
        
        def dfs(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False
            
            return(

            #check left subtree
            dfs(node.left, low, node.val)
            and
            #check right subtree
            dfs(node.right, node.val, high)

            )
        return dfs(root, float("-inf"), float("inf"))