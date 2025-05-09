from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents):
        n = len(parents)
        tree = defaultdict(list)

        # create adjacency list 
        for child, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(child)

        self.max_score = 0
        self.count = 0

        def dfs(node): # returns size of node
            score = 1
            size = 1  # Count self
            for child in tree[node]:
                child_size = dfs(child) # recursive call for child
                size += child_size # add to current node size
                score *= child_size # multiply with score

            # child scores computed
            # current node subtree size also computed 

            rest = n - size
            if rest > 0:
                score *= rest

            # simple logic to check for max score count
            if score > self.max_score:
                self.max_score = score
                self.count = 1
            elif score == self.max_score:
                self.count += 1

            return size

        dfs(0)
        return self.count