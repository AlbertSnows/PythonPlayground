"""
875. Koko Eating Bananas
Difficulty: Medium
https://leetcode.com/problems/koko-eating-bananas/

──────────────────────────────────────────────────

Koko loves to eat bananas. There are n piles of bananas, the i^th
pile has piles[i] bananas. The guards have gone and will come back in
h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour,
she chooses some pile of bananas and eats k bananas from that pile. If
the pile has less than k bananas, she eats all of them instead and
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the
bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas
within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

	• 1 <= piles.length <= 10^4

	• piles.length <= h <= 10^9

	• 1 <= piles[i] <= 10^9
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30),
        (([30, 11, 23, 4, 20], 6), 23),
    ]
    for (args, expected) in tests:
        result = sol.minEatingSpeed(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: minEatingSpeed{args} -> {result} (expected {expected})")
