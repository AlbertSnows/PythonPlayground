"""
102. Binary Tree Level Order Traversal
Difficulty: Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

──────────────────────────────────────────────────

Given the root of a binary tree, return the level order traversal of
its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

	• The number of nodes in the tree is in the range [0, 2000].

	• -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
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
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ]
    for (values, expected) in tests:
        root = build_tree(values)
        result = sol.levelOrder(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: levelOrder({values}) -> {result} (expected {expected})")
