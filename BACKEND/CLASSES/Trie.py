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
    
    def find_words(self, available_letters, length):
        r = self.root 
        def dfs(node, word, remaining_length):
            if remaining_length == 0:
                if node.end:
                    matching.append(word)
                return 
            for char, child in node.children.items():
                if char == '*' or char == available_letters[length - remaining_length - 1]:
                    dfs(child, word + char, remaining_length - 1)       
        matching = []
        dfs(r, '', length)
        return matching

