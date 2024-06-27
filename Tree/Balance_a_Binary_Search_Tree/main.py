class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode, inorder: list):
        # Inorder traversal to store the elements in sorted order
        if not root:
            return
        
        self.inorderTraversal(root.left, inorder)
        inorder.append(root.val)
        self.inorderTraversal(root.right, inorder)
    
    def createBalancedBST(self, inorder: list, start: int, end: int) -> TreeNode:
        # If the start index exceeds the end index
        if start > end:
            return None
        
        # Initialize mid element
        mid = (start + end) // 2

        # Recursively traverse the left subtree
        left_subtree = self.createBalancedBST(inorder, start, mid - 1)
        # Recursively traverse the right subtree
        right_subtree = self.createBalancedBST(inorder, mid + 1, end)

        # Create a new node with the middle element and attach the subtrees
        node = TreeNode(val=inorder[mid], left=left_subtree, right=right_subtree)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Stores the inorder traversal of the BST
        inorder = []
        self.inorderTraversal(root, inorder)

        return self.createBalancedBST(inorder, 0, len(inorder) - 1)



if __name__ == '__main__':
    a = TreeNode(val=1)
    b = TreeNode(val=2)
    c = TreeNode(val=3)
    d = TreeNode(val=4)

    a.right = b
    b.right = c
    c.right = d

    result = Solution().balanceBST(a)
    print(result)