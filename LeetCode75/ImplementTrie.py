class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:

        cur = self.trie

        for i, letter in enumerate(word):
            
            if letter not in cur:
                cur[letter] = {}

            if i == len(word) - 1:
                cur[letter.upper()] = {}

            cur = cur[letter]
        

    def search(self, word: str) -> bool:

        cur = self.trie

        for i, letter in enumerate(word):

            if letter not in cur or i == len(word) - 1 and letter.upper() not in cur:
                return False

            cur = cur[letter]

        return True

    def startsWith(self, prefix: str) -> bool:

        cur = self.trie

        for letter in prefix:

            if letter not in cur:
                return False

            cur = cur[letter]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)