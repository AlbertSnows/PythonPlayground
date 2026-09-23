"""
235. Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

──────────────────────────────────────────────────

Given a binary search tree (BST), find the lowest common ancestor
(LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: &ldquo;The lowest
common ancestor is defined between two nodes p and q as the lowest
node in T that has both p and q as descendants (where we allow a node
to be a descendant of itself).&rdquo;

 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

 

Constraints:

	• The number of nodes in the tree is in the range [2, 10^5].

	• -10^9 <= Node.val <= 10^9

	• All Node.val are unique.

	• p != q

	• p and q will exist in the BST.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass


def build_tree(values):
    """Builds a tree from LeetCode's level-order list format (None = no node).
    Returns (root, node_by_val) so callers can grab specific p/q node references."""
    node_by_val = {}
    if not values or values[0] is None:
        return None, node_by_val
    root = TreeNode(values[0])
    node_by_val[values[0]] = root
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                node_by_val[values[i]] = node.left
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                node_by_val[values[i]] = node.right
                queue.append(node.right)
            i += 1
    return root, node_by_val


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ]
    for (values, p_val, q_val, expected) in tests:
        root, node_by_val = build_tree(values)
        p = node_by_val[p_val]
        q = node_by_val[q_val]
        result_node = sol.lowestCommonAncestor(root, p, q)
        result = result_node.val if result_node else None
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lowestCommonAncestor(tree, {p_val}, {q_val}) -> {result} (expected {expected})")
