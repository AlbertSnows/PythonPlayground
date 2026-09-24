"""
3. Longest Substring Without Repeating Characters
Difficulty: Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/

──────────────────────────────────────────────────

Given a string s, find the length of the longest substring without
duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that
"bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence
and not a substring.

 

Constraints:

	• 0 <= s.length <= 10^5

	• s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a string s, find the length of the longest substring without
        # duplicate characters.

        # Input: s = "abcabcbb"
        # Output: 3
        # Explanation: The answer is "abc", with the length of 3. Note that
        # "bca" and "cab" are also correct answers.
        left = 0
        right = 1
        longest_substring = 1
        end = len(s) - 1
        current_letters: set[str] = set()
        current_letters.add(s[0])
        current_substring = 1
        while right <= end:
            right_letter = s[right]
            already_seen = right_letter in current_letters
            if already_seen:
                current_letters.remove(s[left])
                current_substring -= 1
                left += 1
            else: 
                current_letters.add(right_letter)
                current_substring += 1
                longest_substring = max(longest_substring, current_substring)
                right += 1

        
        return longest_substring


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
    ]
    for (args, expected) in tests:
        result = sol.lengthOfLongestSubstring(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lengthOfLongestSubstring{args} -> {result} (expected {expected})")
