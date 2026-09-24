"""
238. Product of Array Except Self
Difficulty: Medium
https://leetcode.com/problems/product-of-array-except-self/

──────────────────────────────────────────────────

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except
nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using
the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

	• 2 <= nums.length <= 10^5

	• -30 <= nums[i] <= 30

• The input is generated such that answer[i] is guaranteed to fit in
a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity
analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #         Example 1:

        # Input: nums = [1, 3, 2, 4]
        # Output:       [24,8,12, 6]
        outcome = []
        # 1,   3,  2,  4
        # 1,   1,  3,  6
        # 1,   4,  8, 24
        # 24,  8, 12,  6
        prefix = [1]
        for i in range(1, len(nums)):
            current_mult = nums[i - 1]
            prior_size = prefix[i - 1]
            new_mult = current_mult * prior_size
            prefix.append(new_mult)

        nums_len = len(nums)
        suffix = [1]
        for i in reversed(range(1, nums_len)): # 3 2 1 
            # 1, 3, 2, 4
            # 1, 4, 8, 24
            current_mult = nums[i] # 1
            prior_size = suffix[nums_len - i - 1]
            new_mult = current_mult * prior_size
            suffix.append(new_mult)
        for i in range(len(nums)):
            mult_outcome = prefix[i] * suffix[nums_len - i - 1]
            outcome.append(mult_outcome)

        return outcome


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([1, 3, 2, 4],), [24, 8, 12, 6]),
        (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    ]
    for (args, expected) in tests:
        result = sol.productExceptSelf(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: productExceptSelf{args} -> {result} (expected {expected})")
