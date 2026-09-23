"""
300. Longest Increasing Subsequence
Difficulty: Medium
https://leetcode.com/problems/longest-increasing-subsequence/

──────────────────────────────────────────────────

Given an integer array nums, return the length of the longest
strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Example 4:

Input: nums = [3, 1, 2, 2, 2, 3, 1, 2]
Output: 5

 

Constraints:

    • 1 <= nums.length <= 2500

    • -10^4 <= nums[i] <= 10^4

 

Follow up: Can you come up with an algorithm that runs in O(n log(n))
time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        unique_nums = 1
        # 1, 1, 2, 2, 2, 3, 
        max_at_index = [1]
        max_for_num = {};
        for index in range(1, len(nums) - 1):
            current_num = nums[index]
            previous_num = nums[index - 1]
            is_larger = previous_num < current_num
            is_equal = previous_num == current_num
            already_visited = current_num in max_for_num.keys()
            if not already_visited:
                if is_larger:
                    max_for_current_num = max_for_num[previous_num] + 1
                    max_for_num[current_num] = max_for_current_num
                    max_at_index.append(max_for_current_num)
                # elif is_equal: # can't happen 
                else: # is smaller
                    max_at_index.append(max_for_num[current_num])
            else: # seen this number before
                if is_larger:
                    max_for_current_num = max(max_for_num[previous_num] + 1, max_for_num[current_num])
                    max_for_num[current_num] = max_for_current_num
                    max_at_index.append(max_for_current_num)
                elif is_equal: 
                    max_at_index.append(max_for_num[current_num])
                else: # is smaller
                    max_at_index.append(max_for_num[current_num])
        end = len(max_at_index) - 1
        return max_at_index[end]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        (([0, 1, 0, 3, 2, 3],), 4),
        (([7, 7, 7, 7, 7, 7, 7],), 1),
        (([3, 1, 2, 2, 2, 3, 1, 2],), 5),
    ]
    for (args, expected) in tests:
        result = sol.lengthOfLIS(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lengthOfLIS{args} -> {result} (expected {expected})")
