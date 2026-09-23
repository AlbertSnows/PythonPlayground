"""
198. House Robber
Difficulty: Medium
https://leetcode.com/problems/house-robber/

──────────────────────────────────────────────────

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without
alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob
house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Example 3:

Input: nums = [2,1,8,12,3]
Output: 14
Explanation: 2, 12



Constraints:

    • 1 <= nums.length <= 100

    • 0 <= nums[i] <= 400
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        # 2, 2, 10, 14, 13
        start = 2
        max_value_at_index = [nums[0], max(nums[0], nums[1])]
        for index in range(start, len(nums)):
            value_at_index = nums[index]
            previous_max_location = index - 2
            previous_max = max_value_at_index[previous_max_location]
            new_possible_max = previous_max + value_at_index
            max_value_at_index.append(new_possible_max)

        end = len(max_value_at_index) - 1
        return max(max_value_at_index[end], max_value_at_index[end - 1])
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1])) # 4
    print(sol.rob([2, 7, 9, 3, 1])) # 12
    