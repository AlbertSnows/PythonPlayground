"""
200. Number of Islands
Difficulty: Medium
https://leetcode.com/problems/number-of-islands/

──────────────────────────────────────────────────

Given an m x n 2D binary grid grid which represents a map of '1's
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 300

	• grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    sol = Solution()
    tests = [
        ((grid1,), 1),
        ((grid2,), 3),
    ]
    for (args, expected) in tests:
        result = sol.numIslands(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: numIslands(grid) -> {result} (expected {expected})")
