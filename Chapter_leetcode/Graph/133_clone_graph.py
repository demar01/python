"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
       # this is an undirected graph 
       # [[2,4],[1,3],[2,4],[1,3]] this is how we transverse the graph. We need to traverse all the nodes. 
       # we have initialize ref node and build neighbors from scratch
        if not node:
            return node
        seen = {} # value of the node: node itself {int, node}
        def dfs(node, seen): # this is a recursive problem
            new_node = Node(node.val, []) #we intialize our node 
            seen[node.val] = new_node #new_node is the reference
            new_neighbors = []
            #now we buid the node's neighbords
            for n in node.neighbors: #have we seen the neighbors?
                if n.val not in seen: #if this happens we call dfs
                    new_neighbors.append(dfs(n,seen))
                else:
                    new_neighbors.append(seen[n.val]) #if we have seen it before we append from our seen dictionary
            new_node.neighbors= new_neighbors #this was empty before, but we make it equal to new_neighbors
            return new_node

        return dfs(node, seen) #this will return new node , but is a copy now. 

# https://www.youtube.com/watch?v=e5tNvT1iUXs
# https://www.youtube.com/watch?v=S46c4KkLwPM