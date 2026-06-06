class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N) | S: O(M)
        # N = Length of s
        # M = Unique characters in s
        max_length = l = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
