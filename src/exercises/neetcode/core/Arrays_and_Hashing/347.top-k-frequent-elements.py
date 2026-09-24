"""
347. Top K Frequent Elements
Difficulty: Medium
https://leetcode.com/problems/top-k-frequent-elements/

──────────────────────────────────────────────────

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]



Constraints:

        • 1 <= nums.length <= 10^5

        • -10^4 <= nums[i] <= 10^4

        • k is in the range [1, the number of unique elements in the array].

        • It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n
log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Given an integer array nums and an integer k, return the k most
        # frequent elements. You may return the answer in any order.
        # freq map
        # inverse the freq map
        # take the top until k is exhausted
        nums_to_occurance: dict[int, int] = {}
        for num in nums:
            if num in nums_to_occurance:
                nums_to_occurance[num] += 1
            else:
                nums_to_occurance[num] = 1
        unique_nums = set(nums)
        if len(unique_nums) <= k: 
            return unique_nums

        inverted: dict[int, set[int]] = {}
        for key, v in nums_to_occurance.items():
            if v in inverted:
                inverted[v].add(key)
            else:
                inverted[v] = {key}

        sorted_occurance = sorted(inverted.keys(), reverse=True)
        
        remaining = k
        start = 0
        most_freq_nums = []
        while remaining != 0:
            highest_current = sorted_occurance[start]
            nums_for_freq = inverted[highest_current]
            number_of_highest_for_freq = len(nums_for_freq)

            most_freq_nums.extend(nums_for_freq)
            remaining -= number_of_highest_for_freq
            start += 1
        
        return most_freq_nums


if __name__ == "__main__":
    # Order doesn't matter, so we compare as sets.
    sol = Solution()
    tests = [
        (([1, 1, 1, 2, 2, 3], 2), {1, 2}),
        (([1], 1), {1}),
        (([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), {1, 2}),
    ]
    for args, expected in tests:
        result = sol.topKFrequent(*args)
        status = "PASS" if set(result) == expected else "FAIL"
        print(f"{status}: topKFrequent{args} -> {result} (expected set {expected})")
