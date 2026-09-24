"""
300. Longest Increasing Subsequence
Difficulty: Medium
https://leetcode.com/problems/longest-increasing-subsequence/

──────────────────────────────────────────────────

Given an integer array nums, return the length of the longest
strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,1,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


 

Constraints:

    • 1 <= nums.length <= 2500

    • -10^4 <= nums[i] <= 10^4

 

Follow up: Can you come up with an algorithm that runs in O(n log(n))
time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        max_at_index = [1]
        for current_index in range(1, len(nums)):
            current_num = nums[current_index]
            prior_smaller_index = -1
            current_largest_prior = -1
            for previous_index in range(current_index):            
                previous_num = nums[previous_index]
                is_smaller = previous_num < current_num
                if is_smaller:
                    max_at_prev_index = max_at_index[previous_index]
                    if max_at_prev_index > current_largest_prior:
                        prior_smaller_index = previous_index
                        current_largest_prior = max_at_prev_index
            if prior_smaller_index != -1:
                max_at_index.append(max_at_index[prior_smaller_index] + 1)
            else:
                max_at_index.append(1)
            # is_larger = previous_num < current_num
            # is_equal = previous_num == current_num
            # already_visited = current_num in max_for_num
            # if not already_visited:
            #     if is_larger:
            #         max_for_current_num = max_for_num.get(previous_num, 0) + 1
            #         max_for_num[current_num] = max_for_current_num
            #         max_at_index.append(max_for_current_num)
            #     # elif is_equal: # can't happen 
            #     else: # is smaller
            #         max_for_current_num = max_for_num[previous_num]
            #         max_at_index.append(max_for_current_num)
            #         max_for_num[current_num] = max_for_current_num
            # else: # seen this number before
            #     if is_larger:
            #         max_for_current_num = max(max_for_num[previous_num] + 1, max_for_num[current_num])
            #         max_for_num[current_num] = max_for_current_num
            #         max_at_index.append(max_for_current_num)
            #     elif is_equal: 
            #         max_at_index.append(max_for_num[current_num])
            #     else: # is smaller
            #         max_at_index.append(max_for_num[current_num])
        end = max(max_at_index)
        return end


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([10, 9, 1, 5, 3, 7, 101, 18],), 4),
        (([0, 1, 0, 3, 2, 3],), 4),
        (([7, 7, 7, 7, 7, 7, 7],), 1),
        (([3, 1, 2, 2, 2, 3, 1, 2],), 3),
    ]
    for (args, expected) in tests:
        result = sol.lengthOfLIS(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lengthOfLIS{args} -> {result} (expected {expected})")
