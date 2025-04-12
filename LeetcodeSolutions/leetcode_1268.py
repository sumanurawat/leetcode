# trie word search, very popular

from typing import List
class TrieNode:
    def __init__(self):
        self.children = {} # char -> TrieNode
        self.is_end = False
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
        node.is_end = True
    
    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_suggestions(self, prefix):
        node = self.find(prefix)
        if not node:
            return []
        return sorted(node.words)[:3]
    
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        results = []
        prefix = ""
        for char in searchWord:
            prefix += char
            results.append(trie.get_suggestions(prefix))
        return results
