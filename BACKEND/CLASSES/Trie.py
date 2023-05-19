class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        r = self.root
        for c in word:
            if c not in r.children:
                r.children[c] = TrieNode()
            r = r.children[c]
        r.end = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        r = self.root
        for c in word:
            if c not in r.children:
                return False
            r = r.children[c]
        return r.end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        r = self.root
        for c in prefix:
            if c not in r.children:
                return False
            r = r.children[c]
        return True
    
    def print_trie(self):
        r = self.root
        print(r.children)