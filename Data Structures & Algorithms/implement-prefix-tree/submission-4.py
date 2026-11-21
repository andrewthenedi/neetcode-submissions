class TrieNode:
    def __init__(self):
        self.children = {}
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
        for key in word:
            if key not in curr.children:
                curr.children[key] = TrieNode()
            curr = curr.children[key]
        curr.hasEnd = True

    def helper(self, word: str, isPrefix: bool) -> bool:
        # T: O(N) | S: O(1)
        curr = self.root
        for key in word:
            if key not in curr.children:
                return False
            curr = curr.children[key]
        return True if isPrefix else curr.hasEnd

    def search(self, word: str) -> bool:
        return self.helper(word, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.helper(prefix, isPrefix=True)
        