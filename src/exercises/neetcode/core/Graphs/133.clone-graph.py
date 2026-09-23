"""
133. Clone Graph
Difficulty: Medium
https://leetcode.com/problems/clone-graph/

──────────────────────────────────────────────────

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node])
of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

 

Test case format:

For simplicity, each node's value is the same as the node's index
(1-indexed). For example, the first node with val == 1, the second
node with val == 2, and so on. The graph is represented in the test
case using an adjacency list.

An adjacency list is a collection of unordered lists used to
represent a finite graph. Each list describes the set of neighbors of
a node in the graph.

The given node will always be the first node with val = 1. You must
return the copy of the given node as a reference to the cloned graph.

 

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node
(val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node
(val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node
(val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node
(val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph
consists of only one node with val = 1 and it does not have any
neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

 

Constraints:

	• The number of nodes in the graph is in the range [0, 100].

	• 1 <= Node.val <= 100

	• Node.val is unique for each node.

	• There are no repeated edges and no self-loops in the graph.

• The Graph is connected and all nodes can be visited starting from
the given node.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pass


def build_graph(adj_list):
    """Builds a graph from LeetCode's adjacency-list format, returns the node with val=1 (or None)."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node):
    """Walks a graph via BFS and returns it in the same adjacency-list format, for comparison."""
    if node is None:
        return []
    visited = {node.val: node}
    queue = [node]
    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)
    return [sorted(n.val for n in visited[v].neighbors) for v in sorted(visited)]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
    ]
    for (adj_list, expected) in tests:
        original = build_graph(adj_list)
        cloned = sol.cloneGraph(original)
        result = graph_to_adj_list(cloned)
        is_actually_cloned = cloned is None or original is None or cloned is not original
        status = "PASS" if result == expected and is_actually_cloned else "FAIL"
        print(f"{status}: cloneGraph({adj_list}) -> {result} (expected {expected})")
