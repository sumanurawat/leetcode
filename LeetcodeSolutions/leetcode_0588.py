class FileNode:
    def __init__(self, isFile = False):
        self.isFile = isFile
        self.content = ""
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> List[str]:
        path_list = path.split('/')[1:]
        if path_list[-1] == "":
            path_list = path_list[:-1]
        current_node = self.root
        for item in path_list:
            current_node = current_node.children[item]
        if current_node.isFile:
            return [path_list[-1]]
        return sorted(current_node.children.keys())

    def mkdir(self, path: str) -> FileNode:
        path_list = path.split('/')[1:]
        current_node = self.root
        for item in path_list:
            if item not in current_node.children:
                current_node.children[item] = FileNode()
            current_node = current_node.children[item]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_list = filePath.split('/')[1:]
        filename = path_list[-1]
        current_node = self.root
        for name in path_list[:-1]:
            current_node = current_node.children[name]
        if filename not in current_node.children:
            current_node.children[filename] = FileNode(isFile=True)
        current_node = current_node.children[filename]
        current_node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        path_list = filePath.split('/')[1:]
        current_node = self.root
        for name in path_list:
            current_node = current_node.children[name]
        return current_node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
