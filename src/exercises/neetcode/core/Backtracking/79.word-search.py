"""
79. Word Search
Difficulty: Medium
https://leetcode.com/problems/word-search/

──────────────────────────────────────────────────

Given an m x n grid of characters board and a string word, return
true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
"ABCCED"
Output: true

Example 2:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

 

Constraints:

	• m == board.length

	• n = board[i].length

	• 1 <= m, n <= 6

	• 1 <= word.length <= 15

• board and word consists of only lowercase and uppercase English
letters.

 

Follow up: Could you use search pruning to make your solution faster
with a larger board?
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    tests = [
        ((board, "ABCCED"), True),
        ((board, "SEE"), True),
        ((board, "ABCB"), False),
    ]
    for (args, expected) in tests:
        result = sol.exist(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: exist(board, {args[1]!r}) -> {result} (expected {expected})")
