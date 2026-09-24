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

from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        # Input: grid = [
        #   ["1","1","0","0","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","1","0","0"],
        #   ["0","0","0","1","1"]
        # ]
        # Output: 3
        visited = [
            [
                False for i in range(len(grid[0]))
            ]
            for o in range(len(grid))
        ]
        print(visited)

        # iterate until a 1 is found and isn't visited
        # when a 1 is found, initiate BFS
        # add u,d,l,r to queue
        # take one off, look at it, if it's a 0 then return
        # once BFS is complete, incriment islands by 1
        number_of_islands = 0
        for row_i in range(len(grid)):
            for column_i in range(len(grid[0])):
                already_visited = visited[row_i][column_i]
                if already_visited:
                    continue
                visited[row_i][column_i] = True
                spot = grid[row_i][column_i]
                is_land = spot == "1"
                if is_land:
                    traverse_island(grid, visited, row_i, column_i)
                    number_of_islands += 1
        return number_of_islands

def traverse_island(grid: list[list[str]], visited: list[list[bool]], row_i: int, column_i: int):
    to_travel = deque()
    to_travel.append((row_i, column_i))
    upper_boundary = 0
    left_boundary = 0
    right_boundary = len(grid[0]) - 1
    lower_boundary = len(grid) - 1

    while len(to_travel) > 0:
        row, col = to_travel.popleft()
        spot = grid[row][col]
        is_land = spot == "1"
        visited[row][col] = True
        if not is_land:
            continue
        up = (row - 1, col)
        if up[0] >= upper_boundary and not visited[up[0]][up[1]]:
            to_travel.append(up)
        down = (row + 1, col)
        if down[0] <= lower_boundary and not visited[down[0]][down[1]]:
            to_travel.append(down)
        left = (row, col - 1)
        if left[1] >= left_boundary and not visited[left[0]][left[1]]:
            to_travel.append(left)
        right = (row, col + 1)
        if right[1] <= right_boundary and not visited[right[0]][right[1]]:
            to_travel.append(right)
    


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
