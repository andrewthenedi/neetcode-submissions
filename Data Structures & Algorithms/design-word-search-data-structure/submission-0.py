class TrieNode:
    def __init__(self):
        self.children = {}
        self.hasEnd = False

class WordDictionary:
    # T: O(N) | S: O(N + T)
    # N = Length of word
    # T = Number of nodes

    def __init__(self):
        # T: O(1) | S: O(T)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # T: O(N) | S: O(1)
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.hasEnd = True

    def search(self, word: str) -> bool:
        # T: O(N) | S: O(N)
        def dfs(node: Optional[TrieNode], startIdx: int) -> bool:
            for i in range(startIdx, len(word)):
                c = word[i]
                if c == '.':
                    for child in node.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.hasEnd
        return dfs(self.root, 0)
