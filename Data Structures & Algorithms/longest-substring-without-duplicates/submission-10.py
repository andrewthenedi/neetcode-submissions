class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N) | S: O(1)
        # N = Length of s
        longest = l = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
