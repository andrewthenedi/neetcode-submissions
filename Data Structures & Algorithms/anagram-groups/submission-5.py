class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(N * M) | S: O(N)
        # N = Number of strs
        # M = Length of the longest str
        ord_to_anagrams = collections.defaultdict(list)
        for s in strs:
            o = [0] * 26
            for c in s:
                o[ord(c) - ord('a')] += 1
            ord_to_anagrams[tuple(o)].append(s)
        return list(ord_to_anagrams.values())
