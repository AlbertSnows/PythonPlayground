"""
78. Subsets
Difficulty: Medium
https://leetcode.com/problems/subsets/

──────────────────────────────────────────────────

Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the
solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

	• 1 <= nums.length <= 10

	• -10 <= nums[i] <= 10

	• All the numbers of nums are unique.
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        pass


if __name__ == "__main__":
    # Order of subsets, and order within each subset, doesn't matter.
    def normalize(groups):
        return sorted(tuple(sorted(g)) for g in groups)

    sol = Solution()
    tests = [
        (([1, 2, 3],), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        (([0],), [[], [0]]),
    ]
    for (args, expected) in tests:
        result = sol.subsets(*args)
        status = "PASS" if normalize(result) == normalize(expected) else "FAIL"
        print(f"{status}: subsets{args} -> {result} (expected {expected})")
