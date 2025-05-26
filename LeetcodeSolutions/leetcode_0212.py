from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the word at the end node for easy retrieval

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie from the list of words
        trie = Trie()
        for word in words:
            trie.insert(word)
        root = trie.root
        m, n = len(board), len(board[0])
        result = set()

        def dfs(i, j, node):
            # If out of bounds or already visited or char not in Trie, return
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
                return
            char = board[i][j]
            next_node = node.children[char]
            # If we found a word, add to result
            if next_node.word:
                result.add(next_node.word)
                # Optional: remove word to avoid duplicate work
                next_node.word = None
            # Mark as visited
            board[i][j] = '#'
            # Explore neighbors (up, down, left, right)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                dfs(ni, nj, next_node)
            # Restore the character after DFS
            board[i][j] = char
            # Optional: prune the Trie node if no children left
            if not next_node.children:
                node.children.pop(char)

        # Start DFS from every cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return list(result)

# Approach:
# 1. Build a Trie from the list of words for efficient prefix and word lookup.
# 2. For each cell in the board, start a DFS if the letter is a prefix in the Trie.
# 3. During DFS, mark cells as visited and check the Trie for word completion.
# 4. Add found words to the result and optionally remove them from the Trie to avoid duplicates.
# 5. Restore the board after each DFS call.
#
# Time Complexity: O(M*N*4^K), where M,N are board dimensions and K is max word length (<=10).
# Space Complexity: O(L), where L is the total length of all words (for the Trie).
