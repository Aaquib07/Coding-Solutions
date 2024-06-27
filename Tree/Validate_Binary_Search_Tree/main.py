from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Stores the root node, lower limit, upper limit
        stack = [(root, float('-inf'), float('inf'))]
        
        # Iterate until stack gets empty
        while stack:
            # Extract the node, lower limit and upper limit
            node, low, high = stack.pop()
            
            # If the node value goes beyond the limits, it is not a BST
            if not (low < node.val < high):
                return False
            
            # If the node has left subtree
            if node.left:
                # Add the left subtree to the stack along with the corresponding lower and upper limit
                stack.append((node.left, low, node.val))
            # If the node has right subtree
            if node.right:
                # Add the right subtree to the stack along with the corresponding lower and upper limit
                stack.append((node.right, node.val, high))
        
        # The tree is a BST
        return True



if __name__ == '__main__':
    root = TreeNode(5)
    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(3)
    d = TreeNode(6)

    root.left = a
    root.right = b
    b.left = c
    b.right = d

    result = Solution().isValidBST(root)
    print(result)