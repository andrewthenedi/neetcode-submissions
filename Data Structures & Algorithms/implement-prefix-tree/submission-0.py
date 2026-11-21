class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.hasEnd = False

class PrefixTree:
    # T: O(N) | S: O(T)
    # N = Length of word
    # T = Number of nodes

    def __init__(self):
        # T: O(1) | S: O(T)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # T: O(N) | S: O(1)
        curr = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not curr.children[key]:
                curr.children[key] = TrieNode()
            curr = curr.children[key]
        curr.hasEnd = True

    def helper(self, s: str, isPrefix: bool) -> bool:
        # T: O(N) | S: O(1)
        curr = self.root
        for c in s:
            key = ord(c) - ord('a')
            if not curr.children[key]:
                return False
            curr = curr.children[key]
        return True if isPrefix else curr.hasEnd

    def search(self, word: str) -> bool:
        return self.helper(word, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.helper(prefix, isPrefix=True)
        