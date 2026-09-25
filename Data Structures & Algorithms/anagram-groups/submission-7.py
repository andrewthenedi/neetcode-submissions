class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(M * N) | S: O(M)
        # M = Size of strs
        # N = Size of the longest str in strs
        ord_to_anagram = collections.defaultdict(list)
        for s in strs:
            ord_s = [0] * 26
            for c in s:
                ord_s[ord(c) - ord('a')] += 1
            ord_to_anagram[tuple(ord_s)].append(s)
        return list(ord_to_anagram.values())
