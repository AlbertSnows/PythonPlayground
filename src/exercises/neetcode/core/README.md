# Core Pattern Concepts

Quick reference for the problem-solving pattern behind each category in this folder. The goal isn't to memorize solutions — it's to recognize which pattern a new problem belongs to, then apply the general shape.

## 1-D Dynamic Programming

**Core idea**: Break a problem into overlapping subproblems along a single sequence, where the answer at position `i` depends on answers at earlier positions. Build a table (or two rolling variables) bottom-up, or memoize a recursive top-down solution.

**How to spot it**: "What's the max/min/count of ways to do X up to index i" phrasing, where a greedy or purely combinatorial approach breaks down because choices interact.

**Typical solve**: Define `dp[i]` = the answer considering only the first `i` elements. Find the recurrence relating `dp[i]` to `dp[i-1]`, `dp[i-2]`, etc. Often reducible from O(n) space to O(1) with two rolling variables.

## 2-D Dynamic Programming

**Core idea**: Same as 1-D DP, but the subproblem depends on two indices — often comparing two sequences, or tracking position in a grid.

**How to spot it**: Problems comparing two strings/arrays (edit distance, subsequences) or asking about paths through a grid.

**Typical solve**: Build a 2-D table `dp[i][j]`. Base cases along row 0 / column 0, then fill in based on a recurrence that looks at `dp[i-1][j]`, `dp[i][j-1]`, and/or `dp[i-1][j-1]`.

## Advanced Graphs

**Core idea**: Shortest-path and minimum-spanning-tree problems on weighted graphs, where a plain BFS (which assumes equal edge weight) isn't enough.

**How to spot it**: Weighted edges, "cheapest," "minimum cost," or "shortest time" phrasing on a graph.

**Typical solve**: Dijkstra's algorithm (priority queue, greedily expand the cheapest known path) for non-negative weights; Bellman-Ford when you need to bound the number of edges used or handle negative weights; Union-Find or Prim's/Kruskal's for minimum spanning tree.

## Arrays & Hashing

**Core idea**: Trade time for space using a hash map or hash set to turn an O(n²) lookup/comparison into O(n).

**How to spot it**: "Find pairs/groups that satisfy X," "check for duplicates," "count frequency" — anything where a nested loop is the naive approach.

**Typical solve**: One pass to build a hash map of value → index/count/list, then a second pass (or the same pass) to look up what you need in O(1).

## Backtracking

**Core idea**: Explore a decision tree of choices, going one level deeper at a time, and undoing (backtracking) a choice once its branch is exhausted.

**How to spot it**: "Generate all possible X," "find all combinations/permutations/subsets that satisfy a constraint."

**Typical solve**: Recursive function that makes a choice, recurses, then removes the choice before trying the next option. Prune branches early when a partial solution already violates a constraint.

## Binary Search

**Core idea**: Repeatedly halve a search space that has some monotonic property (sorted, or "if X works then everything past X also works").

**How to spot it**: Sorted array, or a question phrased as "find the minimum/maximum value such that condition holds" — even without an explicitly sorted array, if the condition is monotonic, binary search applies to the *answer space* itself.

**Typical solve**: Maintain `left`/`right` pointers, check the midpoint, and narrow the range based on whether the midpoint satisfies the condition.

## Bit Manipulation

**Core idea**: Use bitwise operators (XOR, AND, OR, shifts) to solve problems in O(1) space or avoid arithmetic overflow/type limitations.

**How to spot it**: Problems about finding a unique element among duplicates, or explicitly forbidding use of built-in arithmetic operators.

**Typical solve**: XOR cancels identical values (`a ^ a = 0`), useful for "find the one that doesn't pair up." Shifts and masks build/extract numbers bit by bit for problems simulating arithmetic manually.

## Graphs

**Core idea**: Model relationships as nodes and edges, then traverse with BFS (shortest path / level-by-level) or DFS (explore as deep as possible, good for connectivity and cycle detection).

**How to spot it**: Grids where you move between adjacent cells, or explicit "graph" structures (course prerequisites, network connections).

**Typical solve**: BFS with a queue for shortest-path/level problems; DFS with recursion or an explicit stack for connectivity, cycle detection, or topological ordering (via post-order DFS or in-degree tracking / Kahn's algorithm).

## Greedy

**Core idea**: At each step, make the locally optimal choice and trust that it leads to a globally optimal solution — valid only when the problem has the right structure (no need to "look back" and revise past choices).

**How to spot it**: "Maximize/minimize X," and a local rule (take the largest, sort and take in order) feels intuitively right — usually provable via exchange argument.

**Typical solve**: Often starts by sorting, then a single pass making the obviously-best choice at each step. The hard part is proving the greedy choice never needs to be undone.

## Heap / Priority Queue

**Core idea**: Maintain a data structure that gives O(log n) insert and O(1) access to the min or max element, useful when you repeatedly need "the current smallest/largest" as data streams in or changes.

**How to spot it**: "Kth largest/smallest," "top K," or scheduling problems where you always act on the most urgent/least urgent item next.

**Typical solve**: Push elements onto a min-heap or max-heap; pop the top when you need the current extreme. For "kth largest," maintain a heap of size k.

## Intervals

**Core idea**: Sort intervals by start (or end) time, then sweep through in order, merging or comparing adjacent intervals.

**How to spot it**: Problems involving ranges/intervals that can overlap — meetings, scheduling, merging ranges.

**Typical solve**: Sort by start time. Walk through, and if the current interval overlaps the previous one (or the running merged interval), combine them; otherwise start a new group.

## Linked List

**Core idea**: Manipulate node pointers directly, often using two pointers moving at different speeds (fast/slow) or holding onto previous/next references to reverse or restructure links.

**How to spot it**: Explicit `ListNode` structure, and the problem is about restructuring, reversing, detecting cycles, or finding a specific position without random access.

**Typical solve**: Fast/slow pointer pattern for cycle detection or finding the middle. Three-pointer (prev/curr/next) pattern for in-place reversal. Dummy head node to simplify edge cases at the list's start.

## Math & Geometry

**Core idea**: No single algorithmic trick — these problems test careful simulation of a mathematical or spatial process (matrix rotation, coordinate manipulation) without off-by-one or overflow errors.

**How to spot it**: Problems about matrices, coordinates, or numeric operations with explicit constraints on overflow/precision.

**Typical solve**: Work out the index/coordinate transformation on paper first (e.g., rotating a matrix in place via transpose + reverse), then implement carefully with attention to boundaries.

## Sliding Window

**Core idea**: Maintain a window (subarray/substring) defined by two pointers, expanding the right edge and contracting the left edge based on a condition, to avoid recomputing from scratch for every possible window.

**How to spot it**: "Longest/shortest substring/subarray that satisfies X" — a nested-loop brute force would be O(n²), and the condition can be checked incrementally as the window changes.

**Typical solve**: Expand the right pointer, updating window state (a running sum, a character-count map). When the window becomes invalid, shrink from the left until it's valid again, tracking the best window seen.

## Stack

**Core idea**: Process elements in a way where you need to remember the most recent unresolved item — matching, nesting, or "next greater/smaller element" problems where a stack's LIFO order matches the problem's natural structure.

**How to spot it**: Parentheses/bracket matching, or "find the next element that is greater/smaller than the current one" (monotonic stack).

**Typical solve**: Push elements on; when a new element resolves/matches the top of the stack, pop it. For monotonic stack problems, maintain the stack in increasing or decreasing order, popping elements that violate that order as you go.

## Trees

**Core idea**: Recursive traversal — a tree problem's solution is usually expressible in terms of the same problem solved on its left and right subtrees.

**How to spot it**: Explicit `TreeNode` structure; problems about depth, paths, structure comparison, or ordering.

**Typical solve**: Write a recursive function that returns whatever info the parent needs (depth, a boolean, a min/max range) from each subtree, then combine those results at the current node. BFS with a queue for level-by-level problems instead of pure recursion.

## Tries

**Core idea**: A tree structure specialized for strings, where each path from the root spells out a prefix — enables fast prefix lookups that a hash set can't do efficiently.

**How to spot it**: Problems about prefixes, autocomplete, or searching a large dictionary of words with wildcard/prefix support.

**Typical solve**: Each node holds a map of character → child node, plus a flag marking "a word ends here." Insert/search walk character by character, creating or following child nodes.

## Two Pointers

**Core idea**: Use two indices moving through a sequence (toward each other, or both forward at different speeds) to avoid a nested-loop brute force.

**How to spot it**: Sorted array problems asking about pairs/triples summing to a target, or problems comparing elements from both ends of a sequence.

**Typical solve**: Start pointers at both ends (or one at the start, tracking a second condition). Move the pointer(s) based on a comparison with the target, narrowing the search space each step instead of checking every pair.
