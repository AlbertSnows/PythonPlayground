"""
98. Validate Binary Search Tree
Difficulty: Medium
https://leetcode.com/problems/validate-binary-search-tree/

──────────────────────────────────────────────────

Given the root of a binary tree, determine if it is a valid binary
search tree (BST).

A valid BST is defined as follows:

• The left subtree of a node contains only nodes with keys strictly
less than the node's key.

• The right subtree of a node contains only nodes with keys strictly
greater than the node's key.

	• Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value
is 4.

 

Constraints:

	• The number of nodes in the tree is in the range [1, 10^4].

	• -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        pass


def build_tree(values):
    """Builds a tree from LeetCode's level-order list format (None = no node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
    ]
    for (values, expected) in tests:
        root = build_tree(values)
        result = sol.isValidBST(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: isValidBST({values}) -> {result} (expected {expected})")
