"""
62. Unique Paths
Difficulty: Medium
https://leetcode.com/problems/unique-paths/

──────────────────────────────────────────────────

There is a robot on an m x n grid. The robot is initially located at
the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only
move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique
paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or
equal to 2 * 10^9.

 

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to
reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

 

Constraints:

	• 1 <= m, n <= 100
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math problem
        # 1, 1 = 1
        # 1, 2 = 1
        # 2, 2 = 2
        # 3, 2 = 3
        # 2, 3 = 3
        # 3, 3 = 1, 2, 2, 1 = 6
        # [[o o o]
        #  [o o o]
        #  [o o o]]
        # find all possible combinations = combinatorics
        # binomial coefficient
        # What is a binomial coefficient?
        # C(n, k) reads as "n choose k"
        # choose k elements from a fixed set of n elements
        # for n = 7, k = 3, we get n * (n - 1) * (n - 2) = n! - (n-k)! / (2n)
        # Considerations
        # 1) every path is a combination of R and D
        # 2) every path takes n - 1 -> moves and m -1 \|/ moves, so the total 
        #   number of moves is m + n - 2
        # 3) RRD and RDR are the same components, but different paths. they're unique paths
        # 4) m and n are complimentary, if you take m number of moves, that leaves n remaining
        # 5) so we only care about choosing either m or n - 1 moves

        return math.comb(m + n - 2, m - 1)

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to
# reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

        pass


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ((3, 7), 28),
        ((3, 2), 3),
    ]
    for (args, expected) in tests:
        result = sol.uniquePaths(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: uniquePaths{args} -> {result} (expected {expected})")
