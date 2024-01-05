class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie[None] = {}

    def search(self, word: str) -> bool:
        trie = self.trie

        def searchTrie(word, trie):
            for idx, c in enumerate(word):
                if c not in trie:
                    if c == ".":
                        for sub_trie in trie.values():
                            if searchTrie(word[idx+1:], sub_trie):
                                return True
                    return False
                trie = trie[c]
            if None not in trie:
                return False

            return True
            
        return searchTrie(word, trie)        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)