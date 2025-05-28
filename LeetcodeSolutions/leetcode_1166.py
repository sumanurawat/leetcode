class TrieNode():
    def __init__(self, value=-1):
        self.value = value
        self.next = {}
class Trie():
    def __init__(self):
        self.root = TrieNode()

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        steps = path.split('/')[1:]
        current_node = self.trie.root
        for step in steps[:-1]:
            if step not in current_node.next:
                return False
            current_node = current_node.next[step]
        # if path already exists
        if steps[-1] in current_node.next:
            if current_node.next[steps[-1]].value > 0:
                return False 
            else:
                current_node.next[steps[-1]].value = value
                return True
        current_node.next[steps[-1]] = TrieNode(value)
        return True

    def get(self, path: str) -> int:
        steps = path.split('/')[1:]
        current_node = self.trie.root
        for step in steps:
            if step not in current_node.next:
                return -1
            current_node = current_node.next[step]
        return current_node.value
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)