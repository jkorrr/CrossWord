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
        matching = []
        def dfs(node, word, remaining_length, matching):
            if remaining_length == 0:
                if node.end:
                    matching.append(word)
                return 
            for char, child in node.children.items():
                if char == available_letters[length - remaining_length] or available_letters[length - remaining_length] == '*':
                    dfs(child, word + char, remaining_length - 1, matching)       
        dfs(r, '', length, matching)
        return matching

# testing
'''
dictionary = ['python', 'java', 'ruby', 'perl', 'swift', 'rust']
available_letters = ['*', '*', 't', '*', 'o', 'n']
word_length = 6
r = Trie()

for word in dictionary:
    r.insert(word)


matching_words = r.find_words(available_letters, word_length)
print(matching_words)
'''