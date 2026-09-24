"""
1143. Longest Common Subsequence
Difficulty: Medium
https://leetcode.com/problems/longest-common-subsequence/

──────────────────────────────────────────────────

Given two strings text1 and text2, return the length of their longest
common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original
string with some characters (can be none) deleted without changing the
relative order of the remaining characters.

	• For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common
to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length
is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length
is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

 Example 3:
 Input: text1 = abcdef, text2 = zycdaeyz
 Output: cde
 Explanation: blah

Constraints:

	• 1 <= text1.length, text2.length <= 1000

	• text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # step 1: get unique characters from each string
        # step 2: remove all characters that are not shared between the strings
        # 
        # observation: the longer string L contains the some part of the smaller string S 
        #   as the substring
        # acde, cdaae
        # how do we derive cde? 
        # start with c
        # iterate through S until c
        # iterate both until mismatch
        # if mismatch, find subsequence for left and right
        # keep whichever is longer
        unique_one = set(text1)
        unique_two = set(text2)
        shared = unique_one & unique_two
        if len(shared) == 0:
            return 0

        left_with_only_common = keep(text1, shared)
        right_with_only_common = keep(text2, shared)
        left_smaller = len(left_with_only_common) <= len(right_with_only_common)
        # acde, cdaae
        smaller = left_with_only_common if left_smaller else right_with_only_common
        larger =  right_with_only_common if left_smaller  else left_with_only_common
        outcome = find_subseq(smaller, larger)
        return outcome

def keep(text, shared):
    return "".join(c for c in text if c in shared)

def find_subseq(smaller: str, larger: str) -> int:
    # e
    # aae
    largest_subseq = 0
    if len(smaller) == 0 or len(larger) == 0:
        return 0
    small_letter = smaller[0]
    large_letter = larger[0]
    # acde, cdaae
    # a
    # aa
    # max = 2
    # c, max = 3
    same_letter = small_letter == large_letter
    if same_letter:
        largest_subseq = 1 + find_subseq(smaller[1:], larger[1:])
    else:
        # max for this letter
        largest_from_moving_smallest = find_subseq(smaller[1:], larger)
        largest_from_moving_largest = find_subseq(smaller, larger[1:])
        largest_subseq += max(largest_from_moving_largest, largest_from_moving_smallest)
        
    return largest_subseq

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length
# is 3.


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (("abcde", "ace"), 3),
        (("abc", "abc"), 3),
        (("abc", "def"), 0),
        (("acde", "cdaae"), 3),
    ]
    for (args, expected) in tests:
        result = sol.longestCommonSubsequence(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: longestCommonSubsequence{args} -> {result} (expected {expected})")
